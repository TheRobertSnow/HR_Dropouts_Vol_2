# Generated by Django 2.2.12 on 2020-05-13 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CaptainConsole', '0032_auto_20200513_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='orderitems',
        ),
        migrations.AddField(
            model_name='orders',
            name='orderitems',
            field=models.CharField(blank=True, max_length=9999),
        ),
    ]
