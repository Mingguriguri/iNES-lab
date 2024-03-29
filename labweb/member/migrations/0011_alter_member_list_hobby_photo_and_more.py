# Generated by Django 4.1.5 on 2024-01-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0010_member_list_hobby_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member_list",
            name="hobby_photo",
            field=models.FileField(blank=True, upload_to="upload/%Y/%m/%d/"),
        ),
        migrations.AlterField(
            model_name="member_list",
            name="main_photo",
            field=models.FileField(blank=True, upload_to="upload/%Y/%m/%d/"),
        ),
    ]
