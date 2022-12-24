# Generated by Django 4.1.2 on 2022-12-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_status_alter_articles_created_alter_articles_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ('number',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='orders',
            name='description',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='image',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='name',
        ),
        migrations.AddField(
            model_name='orders',
            name='adress',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Адрес доставки'),
        ),
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Дата доставки'),
        ),
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.TextField(blank=True, max_length=150, verbose_name='Email заказчика'),
        ),
        migrations.AddField(
            model_name='orders',
            name='items',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Всего товаров'),
        ),
        migrations.AddField(
            model_name='orders',
            name='number',
            field=models.TextField(blank=True, max_length=150, verbose_name='Номер заказа'),
        ),
        migrations.AddField(
            model_name='orders',
            name='person',
            field=models.TextField(blank=True, max_length=150, verbose_name='Имя заказчика'),
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='orders',
            name='time',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='К оплате'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Статус'),
        ),
    ]