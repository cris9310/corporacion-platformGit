# Generated by Django 4.2.8 on 2023-12-30 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Programs', '0007_materias_jornada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='calificacion',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Calificacion'),
        ),
    ]
