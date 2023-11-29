from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(
        max_length=50, unique=True, blank=False, verbose_name="Task"
    )
    description = models.TextField(
        max_length=3000, blank=True, verbose_name="Description"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="author", blank=False
    )
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="executor", null=True, blank=True
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, related_name="status", blank=False
    )
    label = models.ManyToManyField(
        Label, through="TaskLabel", related_name="labels", blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["pk"]


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
