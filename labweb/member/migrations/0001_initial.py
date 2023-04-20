# Generated by Django 4.2 on 2023-04-20 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="member_list",
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
                ("name_text", models.CharField(max_length=20)),
                (
                    "one_sentence_text",
                    models.CharField(default="Good, better, best", max_length=50),
                ),
                ("ID_photo_path_text", models.CharField(max_length=100)),
                (
                    "second_photo_path",
                    models.CharField(default="/static/brain.png", max_length=100),
                ),
            ],
        ),
    ]
