# Generated by Django 3.1.8 on 2021-05-10 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201101_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 10, 9, 24, 33, 743293)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 10, 9, 24, 33, 743251)),
        ),
    ]