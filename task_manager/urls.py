from django.contrib import admin
from django.urls import path, include
from task_manager import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.MainIndexView.as_view(), name="main_index"),
    path("users/", include("task_manager.users.urls")),
    path("login/", views.LoginUserFormView.as_view(), name="login"),
    path("logout/", views.LogoutUserView.as_view(), name="logout"),
    path("statuses/", include("task_manager.statuses.urls")),
    path("tasks/", include("task_manager.tasks.urls")),
    path("labels/", include("task_manager.labels.urls")),
]
