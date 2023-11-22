from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from task_manager.users.forms import CreateUserForm, LoginUserForm, UpdateUserForm
from django.utils.translation import gettext as _


# Create your views here.
class UsersIndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()

        return render(request, "users/index.html", {"users": users})


class CreateUserFormView(View):
    def get(self, request, *args, **kwargs):
        form = CreateUserForm()

        return render(request, "users/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("User successfully registered"))

            return redirect("login_user")

        return render(request, "users/create.html", {"form": form})


class LoginUserFormView(View):
    def get(self, request, *args, **kwargs):
        form = LoginUserForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginUserForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _("You are logged in"))

            return redirect("main_index")

        messages.warning(
            request,
            _(
                "Please enter the correct username and password. "
                "Both fields can be case sensitive."
            ),
        )

        return render(request, "users/login.html", {"form": form})


class LogoutUserFormView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _("You are logged out"))

        return redirect("main_index")


class UpdateUserFormView(View):
    def get(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     messages.warning(request, _("You are not authorized! Please log in."))
        #
        #     return redirect("login_user")

        user_id = kwargs.get("pk")

        if user_id != request.user.pk:
            messages.warning(
                request, _("You do not have permission to change another user.")
            )

            return redirect("users_index")

        user = User.objects.get(pk=user_id)
        form = UpdateUserForm(instance=user)

        return render(request, "users/update.html", {"form": form, "user": user})

    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get("pk")
        user = User.objects.get(pk=user_pk)
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, _("User changed successfully"))

            return redirect("users_index")

        return render(request, "users/update.html", {"form": form, "pk": user_pk})


class DeleteUserFormView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, _("You are not authorized! Please log in."))

            return redirect("login_user")

        user_id = kwargs.get("pk")

        if user_id != request.user.pk:
            messages.warning(
                request, _("You do not have permission to change another user.")
            )

            return redirect("users_index")

        user = User.objects.get(pk=user_id)
        user_fullname = f"{user.first_name} {user.last_name}"

        return render(request, "users/delete.html", {"user_fullname": user_fullname})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get("pk")
        user = User.objects.get(pk=user_id)
        user.delete()
        messages.success(request, _("User deleted successfully"))

        return redirect("users_index")
