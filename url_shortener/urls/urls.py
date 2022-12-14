from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="urls-home"),
    path("list/", views.list, name="urls-list"),
    path("create/", views.create, name="urls-add"),
    path("<str:path>", views.show, name="urls-show"),
]
