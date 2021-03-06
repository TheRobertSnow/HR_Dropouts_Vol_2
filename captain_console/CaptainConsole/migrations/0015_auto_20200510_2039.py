# Generated by Django 3.0.6 on 2020-05-10 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CaptainConsole', '0014_auto_20200510_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='productIDs',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='productID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CaptainConsole.Products'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='productAmount',
            field=models.IntegerField(),
        ),
    ]
