# Generated by Django 3.2.5 on 2021-12-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(default='8328', max_length=4, unique=True),
        ),
    ]