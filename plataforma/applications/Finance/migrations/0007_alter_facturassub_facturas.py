# Generated by Django 4.0.5 on 2024-11-16 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0006_alter_facturassub_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturassub',
            name='facturas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='Finance.facturas'),
        ),
    ]
