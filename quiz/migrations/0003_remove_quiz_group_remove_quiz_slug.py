# Generated by Django 4.0.6 on 2022-08-08 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz_group_alter_quiz_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='group',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='slug',
        ),
    ]
