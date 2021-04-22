# Generated by Django 3.2 on 2021-04-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpskit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kosprojek',
            name='kos_belanja',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='kosprojek',
            name='kos_tanggung',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='mrksatu',
            name='mrksatukosprojek',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
