# Generated by Django 3.2.7 on 2021-09-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0003_auto_20210918_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='gym',
            name='start',
            field=models.TimeField(),
        ),
    ]
