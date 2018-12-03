# Generated by Django 2.1.1 on 2018-11-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(verbose_name='event date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(verbose_name='event time'),
        ),
    ]