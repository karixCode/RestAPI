# Generated by Django 5.1.2 on 2024-11-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True),
        ),
    ]
