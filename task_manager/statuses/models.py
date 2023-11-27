from django.db import models


class Status(models.Model):
    name = models.CharField(
        max_length=50, unique=True, blank=False, verbose_name="Status name"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
        ordering = ["pk"]
