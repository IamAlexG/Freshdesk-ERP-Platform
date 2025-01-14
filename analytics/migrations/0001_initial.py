# Generated by Django 4.2.6 on 2023-10-20 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('total_orders', models.PositiveIntegerField()),
                ('total_spent', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user_agent', models.CharField(blank=True, help_text='e.g. Chrome 98, Windows, TECNO KE5, Android', max_length=255, null=True, verbose_name='User Agent')),
                ('last_activity', models.DateTimeField(blank=True, help_text='Last activity of the device', null=True, verbose_name='Last Activity')),
                ('ip_address', models.GenericIPAddressField(blank=True, default='', help_text='IP address of the device', null=True, verbose_name='IP Address')),
                ('location', models.CharField(blank=True, help_text='Location of the device', max_length=255, null=True, verbose_name='Location')),
                ('timezone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Timezone')),
            ],
            options={
                'verbose_name': 'Device Activity',
                'verbose_name_plural': 'Device Activity',
                'ordering': ('-last_activity',),
            },
        ),
        migrations.CreateModel(
            name='InventoryAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('stock_level', models.PositiveIntegerField()),
                ('stockout_count', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('sales_volume', models.PositiveIntegerField()),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('windows', models.IntegerField(default=0)),
                ('mac', models.IntegerField(default=0)),
                ('linux', models.IntegerField(default=0)),
                ('android', models.IntegerField(default=0)),
                ('ios', models.IntegerField(default=0)),
                ('other', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Visitor',
                'verbose_name_plural': 'Visitors',
            },
        ),
    ]
