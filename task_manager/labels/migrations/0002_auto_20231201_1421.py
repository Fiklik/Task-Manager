# Generated by Django 4.2.7 on 2023-12-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("labels", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Label",
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
                    "name",
                    models.CharField(max_length=50, unique=True, verbose_name="Name"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
            ],
            options={
                "verbose_name": "Label",
                "verbose_name_plural": "Labels",
                "ordering": ["pk"],
            },
        ),
    ]
