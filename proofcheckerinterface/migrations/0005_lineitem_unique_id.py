# Generated by Django 5.0 on 2023-12-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proofcheckerinterface", "0004_alter_lineitem_assumption_dependence_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="lineitem",
            name="unique_id",
            field=models.CharField(default="", max_length=255),
        ),
    ]
