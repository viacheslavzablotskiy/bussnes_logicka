# Generated by Django 4.1.4 on 2022-12-23 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docker_docker_admin', '0011_rename_price_dena_trade_price_total_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='item',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='item_1',
        ),
    ]
