# Generated by Django 4.2.3 on 2025-02-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_alter_member_list_degree_alter_member_list_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_list',
            name='email',
            field=models.EmailField(blank=True, default='@gachon.ac.kr', max_length=254, null=True),
        ),
    ]
