# Generated by Django 4.2.8 on 2024-01-20 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Programs', '0012_banner_cod_tarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='observacion',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
