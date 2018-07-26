from django.shortcuts import render, get_object_or_404
from .models import TbFullTimeMage, TbNovel
from .public import get_content, relation

# Create your views here.
def index(request):
    novels = TbNovel.objects.all()
    return render(request, "novel/index.html", context=locals())

def novel_detail(request, novelId):
    novelObj = get_object_or_404(TbNovel, pk=novelId)
    chapterTable = relation.get(novelObj.chapter_table)
    chapters = chapterTable.objects.all()

    return render(request, "novel/novel.html", context={
        "novel" : novelObj,
        "chapters":chapters,
    })

def chapter_detail(request, novelId, chapterId):
    novelObj = get_object_or_404(TbNovel, pk=novelId)
    chapterTable = relation.get(novelObj.chapter_table)
    chapterObj = get_object_or_404(chapterTable, pk=chapterId)

    content = get_content(chapterObj.chapter_url)
    if not content: content = "内容正在手打中, 请稍后..."
    print(content)

    return render(request, "novel/chapter.html", context={
        "chapter" : chapterObj,
        "chapter_content" : content,
    })