# Generated by Django 3.1.5 on 2021-01-12 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0006_auto_20210112_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocabulary',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='vocabulary',
            name='write_time',
        ),
    ]
