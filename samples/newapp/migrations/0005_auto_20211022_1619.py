# Generated by Django 2.0.9 on 2021-10-22 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_product_shop_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_sub',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
