# Generated by Django 5.1.3 on 2024-11-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0002_auto_20240930_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
