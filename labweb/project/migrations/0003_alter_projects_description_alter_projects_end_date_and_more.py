# Generated by Django 4.2.3 on 2024-07-18 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_alter_member_list_degree_alter_member_list_name'),
        ('project', '0002_alter_projects_areas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_lead', to='member.member_list'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
