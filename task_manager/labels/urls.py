from django.urls import path
from task_manager.labels import views


urlpatterns = [
    path("", views.LabelsListView.as_view(), name="labels_list"),
    path("create/", views.CreateLabelView.as_view(), name="create_label"),
    path("<int:pk>/update/", views.UpdateLabelView.as_view(), name="update_label"),
    path("<int:pk>/delete/", views.DeleteLabelView.as_view(), name="delete_label"),
]
