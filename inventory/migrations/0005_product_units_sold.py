# Generated by Django 3.1.6 on 2021-02-15 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210215_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='units_sold',
            field=models.IntegerField(default=0),
        ),
    ]
