# Generated by Django 4.2.3 on 2024-07-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='team',
            field=models.CharField(choices=[('AI', 'AI Team'), ('HW', 'Hardware Team')], default='HW', max_length=2),
        ),
    ]
