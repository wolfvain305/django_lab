from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    path("", views.index, name="index"),
]