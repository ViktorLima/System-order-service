# Generated by Django 2.2.3 on 2023-01-11 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20230111_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='descricao',
            field=models.TextField(max_length=255),
        ),
    ]