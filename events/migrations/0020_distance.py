# Generated by Django 2.1.1 on 2018-11-26 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_activityinstance_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=3, max_digits=10)),
                ('unit', models.CharField(choices=[('MILES', 'Miles'), ('METERS', 'Meters')], max_length=10)),
                ('activity_instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.ActivityInstance')),
            ],
        ),
    ]
