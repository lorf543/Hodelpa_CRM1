# Generated by Django 3.2.7 on 2021-09-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0005_auto_20210918_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gym',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='time',
        ),
        migrations.AddField(
            model_name='gym',
            name='time_end',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='time_start',
            field=models.TimeField(null=True),
        ),
    ]