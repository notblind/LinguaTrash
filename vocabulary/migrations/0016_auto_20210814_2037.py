# Generated by Django 3.2.6 on 2021-08-14 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0015_dayofweek_holiday'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dayofweek',
            table='dayofweek',
        ),
        migrations.AlterModelTable(
            name='holiday',
            table='holiday',
        ),
    ]
