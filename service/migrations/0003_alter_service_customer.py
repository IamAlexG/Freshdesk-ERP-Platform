# Generated by Django 4.2.6 on 2023-10-20 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_delete_ledger'),
        ('service', '0002_remove_service_net_total_remove_service_total_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer'),
        ),
    ]
