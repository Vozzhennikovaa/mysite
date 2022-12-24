# Generated by Django 4.1.2 on 2022-12-14 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_orders_options_remove_orders_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ('orderstatus',), 'verbose_name': 'Статус заказа', 'verbose_name_plural': 'Статус заказа'},
        ),
        migrations.RemoveField(
            model_name='status',
            name='created',
        ),
        migrations.RemoveField(
            model_name='status',
            name='name',
        ),
        migrations.RemoveField(
            model_name='status',
            name='upload',
        ),
        migrations.AddField(
            model_name='status',
            name='orderstatus',
            field=models.CharField(db_index=True, default=-1.0, max_length=100, verbose_name='Статус заказа'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='main.status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='status',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Ссылка'),
        ),
    ]
