# Generated by Django 2.1.2 on 2018-11-18 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messApp', '0027_auto_20181106_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messApp.Member'),
        ),
    ]