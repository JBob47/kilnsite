# Generated by Django 2.1.1 on 2018-11-16 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-event_date']},
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity',
            field=models.CharField(help_text='Enter Activity', max_length=200, verbose_name='Activity'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='event',
            name='season',
            field=models.CharField(choices=[('SPRING', 'Spring'), ('SUMMER', 'Summer'), ('FALL', 'Fall'), ('WINTER', 'Winter')], max_length=10),
        ),
        migrations.AddField(
            model_name='eventinfo',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]