from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    name = models.CharField(
        max_length=50, unique=True, blank=False, verbose_name="Name"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Label")
        verbose_name_plural = _("Labels")
        ordering = ["pk"]
