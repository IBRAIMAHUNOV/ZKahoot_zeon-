# Generated by Django 4.0.6 on 2022-08-10 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_remove_quiztaker_question_usersanswer_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiztaker',
            name='data_finished',
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question'),
        ),
    ]