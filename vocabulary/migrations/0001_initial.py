# Generated by Django 4.2.7 on 2023-11-21 00:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Vocabulary",
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
                ("create_date", models.DateField(auto_now_add=True)),
                ("write_date", models.DateField(auto_now=True)),
                ("name", models.CharField(max_length=2048)),
                ("like", models.BooleanField(default=False)),
                (
                    "create_id",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "write_id",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="modified_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-like", "-id"],
            },
        ),
        migrations.CreateModel(
            name="Word",
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
                ("create_date", models.DateField(auto_now_add=True)),
                ("write_date", models.DateField(auto_now=True)),
                ("word", models.CharField(max_length=2048)),
                (
                    "create_id",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vocabulary_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="words",
                        to="vocabulary.vocabulary",
                    ),
                ),
                (
                    "write_id",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="modified_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Translation",
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
                ("create_date", models.DateField(auto_now_add=True)),
                ("write_date", models.DateField(auto_now=True)),
                ("translate", models.CharField(max_length=2048)),
                (
                    "create_id",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "word_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="vocabulary.word",
                    ),
                ),
                (
                    "write_id",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="modified_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
