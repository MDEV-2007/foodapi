# Generated by Django 4.2.3 on 2023-08-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='avibale',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
