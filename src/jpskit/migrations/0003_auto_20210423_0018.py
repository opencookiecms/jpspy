# Generated by Django 3.2 on 2021-04-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpskit', '0002_auto_20210423_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laporansiapkerja',
            name='lskhargasebenar',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='mrkdua',
            name='mrkduabayarankemajuan',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='perakuanpwjp',
            name='koswjp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='psmk',
            name='psmkbakikos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='psmk',
            name='psmkbakiwangjaminana',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='psmk',
            name='psmkbakiwangjaminanb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='psmk',
            name='psmkhargajaminana',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='psmk',
            name='psmkhargajaminanb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='psmk',
            name='psmkkosbon',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]