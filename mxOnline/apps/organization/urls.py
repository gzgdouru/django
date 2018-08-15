from django.conf.urls import url, include

from .views import OrgListView

app_name = "org"

urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name="org_list"),
]