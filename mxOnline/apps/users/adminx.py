import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting:
    enable_themes = True    #打开主题功能
    use_bootswatch = True   #


class GlobalSetting:
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"    # 折叠左侧数据库表列表


class EmailVerifyRecordAdmin:
    list_display = ["code", "email", "send_type", "send_time"]
    search_fields = ["code", "email", "send_type"]
    list_filter = ["code", "email", "send_type", "send_time"]


class BannerAdmin:
    list_display = ["title", "image", "url", "index", "add_time"]
    search_fields = ["title", "image", "url", "index"]
    list_filter = ["title", "image", "url", "index", "add_time"]


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
