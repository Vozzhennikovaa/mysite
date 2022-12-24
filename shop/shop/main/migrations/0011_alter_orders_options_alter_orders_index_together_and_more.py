# Generated by Django 4.1.2 on 2022-12-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_orders_options_remove_orders_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ('person',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterIndexTogether(
            name='orders',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='status',
            name='slug',
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Способ получения'),
        ),
        migrations.AlterField(
            model_name='status',
            name='orderstatus',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Статус заказа'),
        ),
        migrations.RemoveField(
            model_name='orders',
            name='slug',
        ),
    ]