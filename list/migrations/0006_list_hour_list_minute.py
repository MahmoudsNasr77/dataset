# Generated by Django 4.1.1 on 2022-09-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_list_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='list',
            name='minute',
            field=models.IntegerField(default=0),
        ),
    ]
