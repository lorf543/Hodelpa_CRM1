# Generated by Django 3.2.7 on 2021-09-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0006_auto_20210918_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gym',
            name='time_end',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='time_start',
        ),
        migrations.AddField(
            model_name='gym',
            name='timeend',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='timestart',
            field=models.TimeField(null=True),
        ),
    ]
