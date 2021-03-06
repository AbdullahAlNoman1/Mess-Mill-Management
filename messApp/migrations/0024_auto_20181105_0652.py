# Generated by Django 2.1.2 on 2018-11-05 00:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('messApp', '0023_auto_20181105_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='timestimp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 5, 0, 52, 8, 356669, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(),
        ),
    ]
