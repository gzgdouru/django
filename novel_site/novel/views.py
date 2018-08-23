from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Novel
from .untis import get_content, get_chapter_table

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class IndexView(View):
    '''
    首页
    '''
    def get(self, request):
        all_novels = Novel.objects.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_novels, 5, request=request)
        novels = p.page(page)

        return render(request, "novel/index.html", context={
            "novels" : novels,
        })


def novel_detail(request, novelId):
    novelObj = get_object_or_404(Novel, pk=novelId)
    chapterTable = get_chapter_table(novelObj.id)
    chapters = chapterTable.objects.all().order_by("-chapter_url")

    return render(request, "novel/novel.html", context={
        "novel" : novelObj,
        "chapters":chapters,
    })

def chapter_detail(request, novelId, chapterId):
    novelObj = get_object_or_404(Novel, pk=novelId)

    chapterTable = get_chapter_table(novelObj.id)
    chapterObj = get_object_or_404(chapterTable, pk=chapterId)

    #取上一章节
    pre_chapter = chapterTable.objects.filter(id__lt=int(chapterId)).first()
    if not pre_chapter: pre_chapter = chapterObj

    #取下一章节
    next_chapter = chapterTable.objects.filter(id__gt=int(chapterId)).first()
    if not next_chapter: next_chapter = chapterObj

    content = get_content(chapterObj.chapter_url)
    if not content: content = "内容正在手打中, 请稍后..."

    return render(request, "novel/chapter.html", context={
        "chapter" : chapterObj,
        "chapter_content" : content,
        "novel" : novelObj,
        "pre_chapter" : pre_chapter,
        "next_chapter" : next_chapter,
    })