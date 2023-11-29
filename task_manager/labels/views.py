from .models import Label
from .forms import LabelForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.utils import AuthRequiredMixin, PermissionForDeletionMixin
from django.utils.translation import gettext as _


class LabelsListView(AuthRequiredMixin, ListView):
    template_name = "labels/index.html"
    model = Label
    context_object_name = "labels"


class CreateLabelView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "labels/create.html"
    form_class = LabelForm
    success_message = _("Label created successfully")
    success_url = reverse_lazy("labels_list")


class UpdateLabelView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "labels/update.html"
    form_class = LabelForm
    model = Label
    success_url = reverse_lazy("labels_list")
    success_message = _("Label was successfully modified.")


class DeleteLabelView(
    PermissionForDeletionMixin, AuthRequiredMixin, SuccessMessageMixin, DeleteView
):
    template_name = "labels/delete.html"
    model = Label
    success_url = reverse_lazy("labels_list")
    success_message = _("Label was successfully deleted.")
    no_permission_message = _("Cannot remove label because it is in use")
    no_permission_redirect_url = reverse_lazy("labels_list")
