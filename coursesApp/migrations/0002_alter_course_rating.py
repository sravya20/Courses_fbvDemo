# Generated by Django 5.0.4 on 2024-04-28 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.FloatField(),
        ),
    ]
