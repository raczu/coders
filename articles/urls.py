from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

app_name = 'articles'

urlpatterns = [
    re_path(r'^$', views.articles_list, name="list"),
    re_path(r'^create/$', views.articles_create, name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.articles_detail, name="detail"),
]

urlpatterns += staticfiles_urlpatterns()
