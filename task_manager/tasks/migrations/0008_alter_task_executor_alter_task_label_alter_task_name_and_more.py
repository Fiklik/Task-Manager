# Generated by Django 4.2.7 on 2023-11-30 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("labels", "0001_initial"),
        ("statuses", "0003_alter_status_name"),
        ("tasks", "0007_tasklabel_alter_task_label"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="executor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="executor",
                to=settings.AUTH_USER_MODEL,
                verbose_name="executor",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="label",
            field=models.ManyToManyField(
                blank=True,
                related_name="labels",
                through="tasks.TaskLabel",
                to="labels.label",
                verbose_name="Label",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="name",
            field=models.CharField(max_length=50, unique=True, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="status",
                to="statuses.status",
                verbose_name="status",
            ),
        ),
    ]
