# Generated by Django 3.0.5 on 2020-04-20 18:28

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0002_responsibility"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="firm",
            field=models.TextField(blank=True, null=True),
        ),
    ]