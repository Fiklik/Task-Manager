from .models import Status
from .forms import StatusForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.utils import AuthRequiredMixin
from django.utils.translation import gettext as _


class StatusesListView(AuthRequiredMixin, ListView):
    template_name = "statuses/index.html"
    model = Status
    context_object_name = "statuses"


class CreateStatusView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "statuses/create.html"
    form_class = StatusForm
    success_url = reverse_lazy("statuses")
    success_message = _("Status successfully created")


class UpdateStatusView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "statuses/update.html"
    form_class = StatusForm
    model = Status
    success_url = reverse_lazy("statuses")
    success_message = _("Status changed successfully")


class DeleteStatusView(AuthRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "statuses/delete.html"
    model = Status
    success_url = reverse_lazy("statuses")
    success_message = _("Status successfully deleted")
