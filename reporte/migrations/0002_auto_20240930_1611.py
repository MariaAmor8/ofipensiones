# Generated by Django 2.2.4 on 2024-09-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadocuenta',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
