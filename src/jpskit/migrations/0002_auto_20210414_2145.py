# Generated by Django 3.1.2 on 2021-04-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpskit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontraktor',
            name='konAlamatExtD',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='konAlamatExtS',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='konMPdisah',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='konMPdisemak',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='konMPlulus',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='konNama',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilJPSNoPendaftaran',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilPPKKhuDua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilPPKKhuSatu',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilPPKKhuTiga',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilPPKNoPendaftaran',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilSPKKKhuDua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilSPKKKhuSatu',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilSPKKKhuTiga',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilSSMNoPendaftaran',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilSSTNoPendaftaran',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kontraktor',
            name='sijilSTBNoPendaftaran',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
