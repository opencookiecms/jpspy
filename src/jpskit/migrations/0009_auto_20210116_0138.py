# Generated by Django 3.1.2 on 2021-01-15 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jpskit', '0008_auto_20210116_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noperolehan',
            name='pegawaiselia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpskit.userprofile'),
        ),
    ]
