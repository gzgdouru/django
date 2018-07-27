from bs4 import BeautifulSoup
import requests
from django.http import Http404
from . import models

relation = {
    "tb_chapter_0" : models.TbChapter0,
    "tb_chapter_1" : models.TbChapter1,
    "tb_chapter_2" : models.TbChapter2,
    "tb_chapter_3" : models.TbChapter3,
    "tb_chapter_4" : models.TbChapter4,
    "tb_chapter_5" : models.TbChapter5,
    "tb_chapter_6" : models.TbChapter6,
    "tb_chapter_7" : models.TbChapter7,
    "tb_chapter_8" : models.TbChapter8,
    "tb_chapter_9" : models.TbChapter9,
}

def get_content(url):
    content = None
    try:
        respon = requests.get(url, headers={
            'user-agent': 'Mozilla/5.0'
        }, timeout=30)
        respon.encoding = "gbk"
        html = respon.text
        soup = BeautifulSoup(html, "html.parser")
        contentNode = soup.find(id="content")
        if contentNode.text: content = str(contentNode)
    except Exception as e:
        print("default_parse_content():{}".format(str(e)))
        raise Http404("页面解析出错!")
    return content

def get_chapter_table(novelId):
    tableName = "tb_chapter_{}".format(int(novelId) % 10)
    return relation.get(tableName)
