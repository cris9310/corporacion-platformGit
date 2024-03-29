# Generated by Django 4.2.8 on 2023-12-12 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_remove_user_documento_alter_user_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogsTypesActivities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=200)),
                ('observaciones', models.CharField(blank=True, max_length=100, null=True, verbose_name='Observacion')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
