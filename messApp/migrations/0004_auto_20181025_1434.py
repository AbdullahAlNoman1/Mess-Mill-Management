# Generated by Django 2.1.2 on 2018-10-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messApp', '0003_auto_20181025_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='timestimp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
