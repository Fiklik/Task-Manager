from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.utils import AuthRequiredMixin, PermissionForChangingAuthorMixin
from django.utils.translation import gettext as _


class TasksListView(AuthRequiredMixin, ListView):
    template_name = "tasks/index.html"
    model = Task
    context_object_name = "tasks"
    form_class = TaskForm


class CreateTaskView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "tasks/create.html"
    form_class = TaskForm
    success_message = _("Task created successfully")
    success_url = reverse_lazy("tasks_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "tasks/update.html"
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy("tasks_list")
    success_message = _("Task was successfully modified")


class DeleteTaskView(
    AuthRequiredMixin, PermissionForChangingAuthorMixin, SuccessMessageMixin, DeleteView
):
    template_name = "tasks/delete.html"
    model = Task
    success_url = reverse_lazy("tasks_list")
    success_message = _("Task was successfully deleted")
    no_permission_message = _("Only its author can delete a task")
    no_permission_redirect_url = reverse_lazy("tasks_list")
