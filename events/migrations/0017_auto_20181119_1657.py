# Generated by Django 2.1.1 on 2018-11-19 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20181119_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burpee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='day',
        ),
        migrations.AddField(
            model_name='day',
            name='burpee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Burpee'),
        ),
    ]
