# Generated by Django 2.2.12 on 2020-05-11 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CaptainConsole', '0016_auto_20200511_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='shoppingCart',
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
    ]
