# Generated by Django 4.2.3 on 2024-07-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0004_area_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='photo',
            field=models.FileField(blank=True, upload_to='upload/area/%Y/%m/%d/'),
        ),
    ]