# Generated by Django 3.1.5 on 2021-01-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0002_auto_20210111_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vocabulary',
            name='write_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
