# Generated by Django 5.0.3 on 2024-03-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceCRM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insert',
            name='repair',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]