# Generated by Django 4.0.5 on 2024-12-30 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0011_nominas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturassub',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='gastos',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='nominas',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='otroingreso',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
