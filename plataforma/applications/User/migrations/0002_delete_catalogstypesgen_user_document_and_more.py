# Generated by Django 4.2.8 on 2023-12-09 00:25

import applications.User.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CatalogsTypesGen',
        ),
        migrations.AddField(
            model_name='user',
            name='document',
            field=models.CharField(default=83949348, max_length=20, validators=[applications.User.validators.validate_cero]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 9, 1, 25, 1, 103255)),
        ),
    ]
