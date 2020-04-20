# Generated by Django 3.0.5 on 2020-04-20 11:35

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FeedbackInfo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
                ("message", models.TextField(blank=True, null=True)),
                ("number", models.IntegerField(blank=True, null=True)),
            ],
            options={"verbose_name_plural": "User Info",},
        ),
    ]
