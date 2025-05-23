# Generated by Django 4.0.5 on 2024-12-28 12:13

import applications.User.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0002_docente_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='nDocument',
            field=models.CharField(default=111, max_length=20, unique=True, validators=[applications.User.validators.validate_cero], verbose_name='Número de cédula'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='docente',
            name='codigo',
            field=models.CharField(max_length=50, unique=True, verbose_name='código'),
        ),
    ]
