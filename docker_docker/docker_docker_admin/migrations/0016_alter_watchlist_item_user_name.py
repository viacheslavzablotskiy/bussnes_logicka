# Generated by Django 4.1.4 on 2022-12-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docker_docker_admin', '0015_watchlist_item_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='item_user_name',
            field=models.CharField(blank=True, max_length=110, null=True),
        ),
    ]
