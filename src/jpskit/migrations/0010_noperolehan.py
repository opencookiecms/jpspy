# Generated by Django 3.1.2 on 2020-12-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpskit', '0009_lsk_mr1_mr2_mr3_projek_psk_ss'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoPerolehan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noperolehan', models.CharField(blank=True, max_length=100, null=True)),
                ('tarikh', models.CharField(blank=True, max_length=50, null=True)),
                ('kaedahperolehan', models.CharField(blank=True, max_length=50, null=True)),
                ('pegawaiselia', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]