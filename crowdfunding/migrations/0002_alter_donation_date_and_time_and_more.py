# Generated by Django 4.0.1 on 2022-04-28 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='date_and_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='feedbacks',
            name='date_and_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='topdonors',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='date_and_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
