from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.db.models import Q

from .models import Novel, NovelCategory
from .untis import get_content, get_chapter_table
from .forms import SearchForm

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

        return render(request, "index.html", context={
            "novels" : novels,
        })


def novel_detail(request, novelId):
    '''
    小说详情
    '''
    novelObj = get_object_or_404(Novel, pk=novelId)
    chapterTable = get_chapter_table(novelObj.id)
    chapters = chapterTable.objects.all().order_by("-chapter_index")

    return render(request, "novel/novel-detail.html", context={
        "novel" : novelObj,
        "chapters":chapters,
    })

def chapter_detail(request, novelId, chapterId):
    '''
    章节详情
    '''
    novelObj = get_object_or_404(Novel, pk=novelId)

    chapterTable = get_chapter_table(novelObj.id)
    chapterObj = get_object_or_404(chapterTable, pk=chapterId)

    #取上一章节
    pre_chapter = chapterTable.objects.filter(novel_id=int(novelId), chapter_index__lt=chapterObj.chapter_index).order_by("-chapter_index").first()
    if not pre_chapter: pre_chapter = chapterObj

    #取下一章节
    next_chapter = chapterTable.objects.filter(novel_id=int(novelId), chapter_index__gt=chapterObj.chapter_index).order_by("chapter_index").first()
    if not next_chapter: next_chapter = chapterObj

    content = get_content(chapterObj.chapter_url)
    if not content: content = "内容正在手打中, 请稍后..."

    return render(request, "novel/chapter-detail.html", context={
        "chapter" : chapterObj,
        "chapter_content" : content,
        "novel" : novelObj,
        "pre_chapter" : pre_chapter,
        "next_chapter" : next_chapter,
    })


class CategoryListView(View):
    '''
    分类列表
    '''
    def get(self, request):
        all_categorys = NovelCategory.objects.all()
        return render(request, "novel/category-list.html", context={
            "categorys" : all_categorys,
        })


class CategoryDetailView(View):
    '''
    分类详细
    '''
    def get(self, request, category_id):
        all_novels = Novel.objects.filter(category_id=category_id)
        return render(request, "novel/category-detail.html", context={
            "novels" : all_novels,
        })


class SearchView(View):
    '''
    小说搜索
    '''
    def post(self, request):
        keyword = request.POST.get("keyword", "")
        all_novels = Novel.objects.filter(Q(novel_name__icontains=keyword)|Q(author__name__icontains=keyword))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_novels, 5, request=request)
        novels = p.page(page)

        return render(request, "index.html", context={
            "novels" : novels,
        })
