# Generated by Django 4.1.5 on 2023-04-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("publication", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="publication_list",
            name="pub_photo_path",
        ),
        migrations.AddField(
            model_name="publication_list",
            name="pub_publisher",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
