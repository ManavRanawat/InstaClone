# Generated by Django 3.2.3 on 2021-06-01 10:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 41, 55, 915771, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 41, 55, 915771, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 41, 55, 915771, tzinfo=utc)),
        ),
    ]
