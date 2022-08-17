# Generated by Django 4.1 on 2022-08-08 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_rename_id_task_task_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='approval_status',
            new_name='ApprovalStatus',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='assigned_manager',
            new_name='AssignedManager',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created_date',
            new_name='CreatedDate',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='end_time',
            new_name='EndTime',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='start_time',
            new_name='StartTime',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='Status',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_id',
            new_name='TaskId',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_name',
            new_name='TaskName',
        ),
    ]
