# Generated by Django 4.1.4 on 2022-12-22 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docker_docker_admin', '0005_offer_total_price_is_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='total_price_item',
        ),
    ]
