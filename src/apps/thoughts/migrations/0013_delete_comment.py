# Generated by Django 3.0.5 on 2020-04-26 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("thoughts", "0012_comment_post_user"),
    ]

    operations = [
        migrations.DeleteModel(name="Comment",),
    ]
