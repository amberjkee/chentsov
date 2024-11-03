# Generated by Django 5.1.2 on 2024-11-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customers',
            options={'verbose_name': 'Заказчик', 'verbose_name_plural': 'Заказчики'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='orders',
            name='is_confirmed',
            field=models.BooleanField(default=False, verbose_name='Статус подтверждения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='Статус доставки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='term_num',
            field=models.IntegerField(default=123, verbose_name='Номер договора'),
            preserve_default=False,
        ),
    ]