from django.conf.urls import url

from .views import AuthorsListView

app_name = "authors"

urlpatterns = [
    url(r'^list/$', AuthorsListView.as_view(), name="authors_list"),
]