# Generated by Django 2.1.3 on 2018-11-16 07:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Chitfund', '0003_auto_20181116_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allotment',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='collection',
            name='date_collected',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]