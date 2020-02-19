from django.urls import path, re_path
from . import views

app_name = 'challenges'

urlpatterns = [
    re_path(r'^$', views.challengesView, name="challenge"),
]