from bs4 import BeautifulSoup
import requests
from django.http import Http404
from .models import TbFullTimeMage, TbBlackTechnologicSystem, TbJidaotianmo, TbMutianji

relation = {
    "tb_full_time_mage" : TbFullTimeMage,
    "tb_black_technologic_system" : TbBlackTechnologicSystem,
    "tb_jidaotianmo" : TbJidaotianmo,
    "tb_mutianji" : TbMutianji,
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