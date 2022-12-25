# Generated by Django 4.1.4 on 2022-12-23 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docker_docker_admin', '0010_price_total_price_price_total_price_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='price_dena',
            new_name='price_total_1',
        ),
        migrations.RemoveField(
            model_name='price',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='total_price_item',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='description',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='quantity',
        ),
        migrations.AddField(
            model_name='trade',
            name='item_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_1', related_query_name='item_1', to='docker_docker_admin.item'),
        ),
        migrations.AddField(
            model_name='trade',
            name='price_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='balans',
            name='balans',
            field=models.DecimalField(blank=True, decimal_places=2, default=400, max_digits=5, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_total_price', related_query_name='item_total_price', to='docker_docker_admin.item'),
        ),
    ]