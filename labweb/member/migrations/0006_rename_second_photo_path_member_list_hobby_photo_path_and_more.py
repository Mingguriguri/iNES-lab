# Generated by Django 4.1.5 on 2023-11-08 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0005_alter_member_list_degree"),
    ]

    operations = [
        migrations.RenameField(
            model_name="member_list",
            old_name="second_photo_path",
            new_name="hobby_photo_path",
        ),
        migrations.RenameField(
            model_name="member_list",
            old_name="ID_photo_path_text",
            new_name="main_photo_path_text",
        ),
        migrations.RenameField(
            model_name="member_list",
            old_name="one_sentence_text",
            new_name="motto",
        ),
        migrations.RenameField(
            model_name="member_list",
            old_name="name_text",
            new_name="name",
        ),
    ]