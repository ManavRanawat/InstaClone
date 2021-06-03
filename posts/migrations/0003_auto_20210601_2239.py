# Generated by Django 3.2.3 on 2021-06-01 17:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210601_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 17, 9, 50, 10351, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 17, 9, 50, 9351, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 17, 9, 50, 8313, tzinfo=utc)),
        ),
    ]
