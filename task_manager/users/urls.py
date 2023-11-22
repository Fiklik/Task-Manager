from django.urls import path
from task_manager.users import views


urlpatterns = [
    path("", views.UsersIndexView.as_view(), name="users_index"),
    path("create/", views.CreateUserFormView.as_view(), name="create_user"),
    path("login/", views.LoginUserFormView.as_view(), name="login_user"),
    path("logout/", views.LogoutUserFormView.as_view(), name="logout_user"),
    path("<int:pk>/update/", views.UpdateUserFormView.as_view(), name="update_user"),
    path("<int:pk>/delete/", views.DeleteUserFormView.as_view(), name="delete_user"),
]
