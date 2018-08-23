from bs4 import BeautifulSoup
import requests
from django.http import Http404
from novel import models

relation = {
    "tb_chapter_0" : models.Chapter0,
    "tb_chapter_1" : models.Chapter1,
    "tb_chapter_2" : models.Chapter2,
    "tb_chapter_3" : models.Chapter3,
    "tb_chapter_4" : models.Chapter4,
    "tb_chapter_5" : models.Chapter5,
    "tb_chapter_6" : models.Chapter6,
    "tb_chapter_7" : models.Chapter7,
    "tb_chapter_8" : models.Chapter8,
    "tb_chapter_9" : models.Chapter9,
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
