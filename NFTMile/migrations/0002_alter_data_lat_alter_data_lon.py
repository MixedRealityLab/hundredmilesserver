# Generated by Django 4.1.7 on 2023-03-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFTMile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='lat',
            field=models.DecimalField(decimal_places=16, max_digits=200),
        ),
        migrations.AlterField(
            model_name='data',
            name='lon',
            field=models.DecimalField(decimal_places=16, max_digits=200),
        ),
    ]
