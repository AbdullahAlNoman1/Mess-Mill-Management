# Generated by Django 2.1.2 on 2018-10-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messApp', '0005_member_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
