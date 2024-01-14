# Generated by Django 5.0 on 2023-12-22 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LineItem",
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
                ("line_number", models.CharField(max_length=255)),
                ("formula", models.CharField(max_length=255)),
                ("justification", models.CharField(max_length=255)),
            ],
        ),
    ]
