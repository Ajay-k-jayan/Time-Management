# Generated by Django 4.1 on 2022-08-10 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='CreatedDate',
        ),
    ]
