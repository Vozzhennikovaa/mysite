# Generated by Django 4.1.2 on 2022-12-14 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_orders_delivery'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Delivery',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]