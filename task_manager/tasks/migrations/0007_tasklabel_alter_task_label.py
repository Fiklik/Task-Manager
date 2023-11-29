# Generated by Django 4.2.7 on 2023-11-29 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("labels", "0001_initial"),
        ("tasks", "0006_alter_task_executor"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskLabel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "label",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="labels.label"
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tasks.task"
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="task",
            name="label",
        ),
        migrations.AddField(
            model_name="task",
            name="label",
            field=models.ManyToManyField(
                blank=True,
                related_name="labels",
                through="tasks.TaskLabel",
                to="labels.label",
            ),
        ),
    ]
