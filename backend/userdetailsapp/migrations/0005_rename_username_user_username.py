# Generated by Django 4.1 on 2022-08-13 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdetailsapp', '0004_rename_password_user_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='UserName',
        ),
    ]