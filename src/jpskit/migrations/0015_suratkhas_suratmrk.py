# Generated by Django 3.1.2 on 2021-02-13 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jpskit', '0014_perakuanpwjp_suratpjaminanbank'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuratMRK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smrkrujukantuan', models.CharField(blank=True, max_length=50, null=True)),
                ('smrktarikh', models.CharField(blank=True, max_length=50, null=True)),
                ('smrkjenisborang', models.CharField(blank=True, max_length=50, null=True)),
                ('smrknamarujukan', models.CharField(blank=True, max_length=50, null=True)),
                ('smkralamatrujukan', models.CharField(blank=True, max_length=50, null=True)),
                ('smrkpegawai', models.CharField(blank=True, max_length=50, null=True)),
                ('smrkjawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('smrkknosebutharga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.noperolehan')),
                ('smrkmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
            ],
            options={
                'verbose_name_plural': 'Surat MRK',
            },
        ),
        migrations.CreateModel(
            name='SuratKhas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('khasrujukantuan', models.CharField(blank=True, max_length=50, null=True)),
                ('khasnamarujukan', models.CharField(blank=True, max_length=50, null=True)),
                ('khasalamatrujukan', models.CharField(blank=True, max_length=50, null=True)),
                ('khaspegawai', models.CharField(blank=True, max_length=50, null=True)),
                ('khasjawatan', models.CharField(blank=True, max_length=50, null=True)),
                ('khasknosebutharga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.noperolehan')),
                ('khasmrksatulink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jpskit.mrksatu')),
            ],
            options={
                'verbose_name_plural': 'Surat Khas',
            },
        ),
    ]
