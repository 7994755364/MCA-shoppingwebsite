# Generated by Django 2.0.9 on 2021-10-22 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_rating_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='SHOP_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='newapp.shops'),
        ),
    ]
