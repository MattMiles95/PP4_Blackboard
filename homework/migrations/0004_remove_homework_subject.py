# Generated by Django 4.2.17 on 2025-02-05 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_remove_homework_status_homework_marked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='subject',
        ),
    ]
