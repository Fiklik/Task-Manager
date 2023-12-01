from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(
        max_length=50, unique=True, blank=False, verbose_name=_("Name")
    )
    description = models.TextField(
        max_length=3000, blank=True, verbose_name=_("Description")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="author", blank=False
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="executor",
        verbose_name=_("executor"),
        null=True,
        blank=True,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="status",
        verbose_name=_("status"),
        blank=False,
    )
    labels = models.ManyToManyField(
        Label,
        through="TaskLabel",
        related_name=_("labels"),
        verbose_name=_("Labels"),
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
        ordering = ["pk"]


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
