# Generated by Django 4.2.17 on 2025-02-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_remove_homework_file_homework_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='status',
        ),
        migrations.AddField(
            model_name='homework',
            name='marked',
            field=models.BooleanField(default=False),
        ),
    ]
