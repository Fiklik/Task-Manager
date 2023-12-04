from django.urls import path
from task_manager.users import views


urlpatterns = [
    path("", views.UsersListView.as_view(), name="users_list"),
    path("create/", views.CreateUserView.as_view(), name="create_user"),
    path("<int:pk>/update/", views.UpdateUserView.as_view(), name="update_user"),
    path("<int:pk>/delete/", views.DeleteUserView.as_view(), name="delete_user"),
]
