# Generated by Django 4.0.6 on 2022-08-08 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_remove_quiztaker_completed_quiztaker_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiztaker',
            name='answer',
        ),
    ]
