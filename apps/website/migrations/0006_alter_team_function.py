# Generated by Django 4.2.7 on 2023-12-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_carrocel_galeria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='function',
            field=models.CharField(default='', max_length=200),
        ),
    ]
