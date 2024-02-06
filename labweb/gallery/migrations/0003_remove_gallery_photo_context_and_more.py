# Generated by Django 4.1.5 on 2024-01-11 04:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0002_alter_gallery_photo_dates"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gallery",
            name="photo_context",
        ),
        migrations.RemoveField(
            model_name="gallery",
            name="photo_dates",
        ),
        migrations.RemoveField(
            model_name="gallery",
            name="photo_title",
        ),
        migrations.AddField(
            model_name="gallery",
            name="contents",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="gallery",
            name="title",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="gallery",
            name="upload_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="photo_path",
            field=models.FileField(blank=True, null=True, upload_to="upload/%Y/%m/%d/"),
        ),
    ]