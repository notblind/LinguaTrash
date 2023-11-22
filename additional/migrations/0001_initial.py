# Generated by Django 4.2.7 on 2023-11-22 21:54

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
            name="DayOfWeek",
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
                ("day_text", models.TextField()),
                (
                    "create_id",
                    models.ForeignKey(
                        blank=True,
                        db_column="create_id",
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
                        db_column="write_id",
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
        migrations.CreateModel(
            name="Holiday",
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
                ("description", models.CharField(max_length=2048)),
                (
                    "create_id",
                    models.ForeignKey(
                        blank=True,
                        db_column="create_id",
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "day_id",
                    models.ForeignKey(
                        db_column="day_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dayofweek",
                        to="additional.dayofweek",
                    ),
                ),
                (
                    "write_id",
                    models.ForeignKey(
                        blank=True,
                        db_column="write_id",
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
        migrations.CreateModel(
            name="FeedBack",
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
                ("text", models.TextField()),
                (
                    "create_id",
                    models.ForeignKey(
                        blank=True,
                        db_column="create_id",
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
                        db_column="write_id",
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