# Generated by Django 2.1.1 on 2018-11-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20181114_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='point_value',
            field=models.IntegerField(verbose_name='point_value'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='rep_standard',
            field=models.IntegerField(blank=True, null=True, verbose_name='rep_standard'),
        ),
    ]
