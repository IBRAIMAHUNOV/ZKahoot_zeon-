# Generated by Django 4.0.6 on 2022-08-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodels',
            name='rating',
        ),
        migrations.AddField(
            model_name='usermodels',
            name='passed_total_test',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='usermodels',
            name='rating_global',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='usermodels',
            name='rating_group',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
