# Generated by Django 3.1.2 on 2020-12-29 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jpskit', '0012_auto_20201229_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='projek',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jpskit.kontraktor'),
            preserve_default=False,
        ),
    ]
