# Generated by Django 2.1.2 on 2018-11-06 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messApp', '0026_auto_20181106_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_as', to='messApp.Member'),
        ),
    ]
