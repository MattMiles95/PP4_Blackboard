# Generated by Django 4.2.17 on 2025-01-28 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_rename_author_comment_teacher_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='excerpt',
            new_name='summary',
        ),
    ]
