# Generated by Django 2.2.12 on 2020-05-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CaptainConsole', '0024_auto_20200513_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentinfo',
            name='creditcardnumber',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='expirationdate',
            field=models.CharField(max_length=50),
        ),
    ]
