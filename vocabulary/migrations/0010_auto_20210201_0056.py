# Generated by Django 3.1.5 on 2021-01-31 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0009_auto_20210113_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vocabulary',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='words',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]