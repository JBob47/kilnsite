# Generated by Django 2.1.1 on 2018-11-26 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20181126_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityinstance',
            name='day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Day'),
        ),
    ]