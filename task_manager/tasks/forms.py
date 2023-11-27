from django import forms
from .models import Task
from task_manager.statuses.models import Status
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    executor = forms.ModelChoiceField(label="Executor", queryset=User.objects.all())
    status = forms.ModelChoiceField(label="Status", queryset=Status.objects.all())

    class Meta:
        model = Task
        fields = ["name", "description", "executor", "status"]
