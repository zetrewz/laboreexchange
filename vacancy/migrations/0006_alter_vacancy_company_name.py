# Generated by Django 5.0 on 2024-01-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0005_vacancy_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='company_name',
            field=models.CharField(max_length=255),
        ),
    ]
