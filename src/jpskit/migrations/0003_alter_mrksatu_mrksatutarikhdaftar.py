# Generated by Django 3.2 on 2021-06-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpskit', '0002_alter_mrksatu_mrksatutarikhmula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mrksatu',
            name='mrksatutarikhdaftar',
            field=models.DateField(blank=True, max_length=50, null=True),
        ),
    ]
