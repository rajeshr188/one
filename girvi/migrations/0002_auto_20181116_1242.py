# Generated by Django 2.1.3 on 2018-11-16 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('girvi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investee', to='contact.Customer'),
        ),
    ]
