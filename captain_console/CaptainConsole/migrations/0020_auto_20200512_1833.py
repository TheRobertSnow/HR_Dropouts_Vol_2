# Generated by Django 3.0.6 on 2020-05-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CaptainConsole', '0019_auto_20200512_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]