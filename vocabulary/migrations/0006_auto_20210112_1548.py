# Generated by Django 3.1.5 on 2021-01-12 12:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vocabulary", "0005_auto_20210112_1547"),
    ]

    operations = [
        migrations.AddField(
            model_name="vocabulary",
            name="create_time",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vocabulary",
            name="write_time",
            field=models.DateField(auto_now=True),
        ),
    ]
