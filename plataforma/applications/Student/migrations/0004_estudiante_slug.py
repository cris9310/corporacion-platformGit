# Generated by Django 4.0.5 on 2024-10-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_remove_graduated_carrera_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
