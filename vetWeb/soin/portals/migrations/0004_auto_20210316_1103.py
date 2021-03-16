# Generated by Django 3.1.3 on 2021-03-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0003_auto_20210312_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artificial_insemination_form',
            name='date_of_pregnancy_diagnosis',
            field=models.DateField(verbose_name='Date of pregnancy diagnosis'),
        ),
        migrations.AlterField(
            model_name='artificial_insemination_form',
            name='reason_for_the_cause_of_abortion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Reeason for the cause of abortion'),
        ),
        migrations.AlterField(
            model_name='artificial_insemination_form',
            name='sire_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Sire`s name'),
        ),
        migrations.AlterField(
            model_name='artificial_insemination_form',
            name='sire_origin',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Sire`s origin'),
        ),
        migrations.AlterField(
            model_name='artificial_insemination_form',
            name='time_of_heat_sign',
            field=models.TimeField(verbose_name='Time of heat sign'),
        ),
        migrations.AlterField(
            model_name='artificial_insemination_form',
            name='time_of_insemination',
            field=models.TimeField(verbose_name='Time of insemination'),
        ),
    ]