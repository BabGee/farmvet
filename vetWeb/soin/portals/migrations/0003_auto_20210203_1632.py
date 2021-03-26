# Generated by Django 3.1.3 on 2021-02-03 16:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0002_auto_20210203_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='death_approach_form',
            name='death_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date the animal died'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='death_approach_form',
            name='death_time',
            field=models.TimeField(verbose_name='At what time the animal the animals died'),
        ),
        migrations.AlterField(
            model_name='death_approach_form',
            name='mortality_rate',
            field=models.CharField(default='', max_length=100),
        ),
    ]
