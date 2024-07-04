# Generated by Django 4.2.3 on 2024-07-04 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_projects_architecture_path_projects_github_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='architecture_path',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='photo_path',
        ),
        migrations.CreateModel(
            name='ProjectPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='upload/project/%Y/%m/%d/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='project.projects')),
            ],
        ),
    ]