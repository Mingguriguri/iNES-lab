# Generated by Django 4.2 on 2023-04-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gallery",
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
                ("photo_title", models.CharField(max_length=20)),
                ("photo_context", models.CharField(max_length=100)),
                (
                    "photo_path",
                    models.CharField(default="/static/brain.png", max_length=100),
                ),
            ],
        ),
    ]