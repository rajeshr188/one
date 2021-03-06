# Generated by Django 2.1.3 on 2018-11-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20181117_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Address',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='relatedto',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='type',
            field=models.CharField(choices=[('Wh', 'Wholesale'), ('Re', 'Retail')], default='Re', max_length=30),
        ),
    ]
