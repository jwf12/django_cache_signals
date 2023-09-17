# Generated by Django 4.2.5 on 2023-09-17 05:49

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0005_carrito_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='number',
            field=shortuuid.django_fields.ShortUUIDField(alphabet=None, length=6, max_length=6, prefix=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='number',
            field=shortuuid.django_fields.ShortUUIDField(alphabet=None, length=6, max_length=6, prefix=''),
        ),
    ]