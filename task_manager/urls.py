from django.contrib import admin
from django.urls import path, include
from task_manager import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.MainIndexView.as_view(), name="main_index"),
    path("users/", include("task_manager.users.urls")),
]
