# Generated by Django 4.2.6 on 2023-10-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='task_complete',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='task_title',
        ),
        migrations.AddField(
            model_name='task',
            name='task_incomplete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='task_inprogress',
            field=models.BooleanField(default=False),
        ),
    ]
