# Generated by Django 4.0.5 on 2024-12-08 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0007_alter_facturassub_facturas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturassub',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
