# Generated by Django 4.2.5 on 2023-09-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0003_remove_carrito_name_producto_precio_itemcarrito_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='items',
        ),
        migrations.AddField(
            model_name='carrito',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carrito',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ItemCarrito',
        ),
    ]
