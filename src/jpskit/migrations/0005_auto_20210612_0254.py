# Generated by Django 3.2 on 2021-06-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpskit', '0004_auto_20210612_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laporansiapkerja',
            name='lskkerjasiap',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laporansiapkerja',
            name='lsklanjutmasa',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laporansiapkerja',
            name='lsktarikhperakui',
            field=models.DateField(blank=True, null=True),
        ),
    ]
