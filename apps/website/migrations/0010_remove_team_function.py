# Generated by Django 4.2.7 on 2023-12-10 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_newletterassinature_team_content_team_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='function',
        ),
    ]
