# Generated by Django 4.2.5 on 2023-09-17 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0004_remove_carrito_items_carrito_name_carrito_precio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
