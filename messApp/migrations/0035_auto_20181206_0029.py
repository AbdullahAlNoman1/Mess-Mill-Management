# Generated by Django 2.1.2 on 2018-12-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messApp', '0034_auto_20181205_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='meal_type',
            field=models.CharField(blank=True, choices=[('breakfast', 'Breakfast'), ('launch', 'Launch'), ('dinner', 'Dinner')], max_length=20, null=True, verbose_name='Expense Type'),
        ),
    ]
