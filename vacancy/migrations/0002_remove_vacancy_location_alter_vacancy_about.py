# Generated by Django 5.0 on 2024-01-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='location',
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='about',
            field=models.CharField(max_length=500),
        ),
    ]
