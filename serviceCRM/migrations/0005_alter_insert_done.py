# Generated by Django 5.0.3 on 2024-03-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceCRM', '0004_alter_insert_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insert',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
