# Generated by Django 4.2.3 on 2024-07-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0013_member_list_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_list',
            name='team',
            field=models.CharField(choices=[('AI', 'AI Team'), ('HW', 'Hardware Team'), ('OT', 'Others')], default='HW', max_length=2),
        ),
    ]
