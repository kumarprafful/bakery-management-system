# Generated by Django 3.1.6 on 2021-02-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.IntegerField(choices=[(1, 'admin'), (2, 'customer')], default=2),
        ),
    ]
