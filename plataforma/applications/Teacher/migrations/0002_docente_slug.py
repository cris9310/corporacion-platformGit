# Generated by Django 4.0.5 on 2024-10-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
