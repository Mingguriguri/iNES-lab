# Generated by Django 4.1.5 on 2024-01-10 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Publication",
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
                ("title", models.CharField(max_length=255)),
                ("citation_text", models.TextField()),
                ("published_date", models.DateTimeField()),
                ("doi_link", models.URLField()),
                (
                    "pub_type",
                    models.CharField(
                        choices=[
                            ("CONF", "Conference"),
                            ("JOUR", "Journal"),
                            ("SURV", "Survey"),
                        ],
                        default="JOUR",
                        max_length=4,
                    ),
                ),
                (
                    "related_project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.projects",
                    ),
                ),
            ],
        ),
    ]
