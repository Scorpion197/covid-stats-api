# Generated by Django 3.2 on 2022-01-02 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='active_cases',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='new_cases',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='new_deaths',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='new_recovered',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='serious_critical',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='total_cases',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='total_deaths',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='total_recovered',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
