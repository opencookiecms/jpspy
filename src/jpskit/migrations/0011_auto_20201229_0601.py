# Generated by Django 3.1.2 on 2020-12-29 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpskit', '0010_noperolehan'),
    ]

    operations = [
        migrations.AddField(
            model_name='projek',
            name='tarikh',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projek',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
