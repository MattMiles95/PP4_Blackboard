# Generated by Django 4.2.17 on 2025-01-29 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_rename_excerpt_lesson_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='teacher',
            new_name='commenter',
        ),
    ]
