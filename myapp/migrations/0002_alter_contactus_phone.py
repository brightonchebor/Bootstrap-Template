# Generated by Django 5.1.3 on 2024-11-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
