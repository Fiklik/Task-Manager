from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.users.models import User
from task_manager.users.forms import CreateUserForm, UpdateUserForm
from django.utils.translation import gettext as _
from task_manager.utils import AuthRequiredMixin, PermissionForChangingUserMixin


# Create your views here.
class UsersListView(ListView):
    """Show all users."""

    template_name = "users/index.html"
    model = User
    context_object_name = "users"
    ordering = ["pk"]


class CreateUserFormView(SuccessMessageMixin, CreateView):
    """Create new user."""

    template_name = "users/create.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    success_message = _("User is successfully registered")


class UpdateUserFormView(
    AuthRequiredMixin, PermissionForChangingUserMixin, SuccessMessageMixin, UpdateView
):
    template_name = "users/update.html"
    form_class = UpdateUserForm
    model = User
    no_permission_redirect_url = reverse_lazy("users_list")
    no_permission_message = _("You do not have permission to change another user.")
    success_url = reverse_lazy("users_list")
    success_message = _("User changed successfully")


class DeleteUserView(
    AuthRequiredMixin, PermissionForChangingUserMixin, SuccessMessageMixin, DeleteView
):
    template_name = "users/delete.html"
    model = User
    success_url = reverse_lazy("users_list")
    success_message = _("User deleted successfully.")
    no_permission_redirect_url = reverse_lazy("users_list")
    no_permission_message = _("You do not have permission to change another user.")
