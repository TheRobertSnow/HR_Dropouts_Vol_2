# Generated by Django 3.0.6 on 2020-05-13 14:43

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('CaptainConsole', '0025_auto_20200513_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
