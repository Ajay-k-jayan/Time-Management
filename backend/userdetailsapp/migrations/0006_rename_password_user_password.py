# Generated by Django 4.1 on 2022-08-13 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdetailsapp', '0005_rename_username_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='Password',
        ),
    ]