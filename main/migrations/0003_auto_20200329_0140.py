# Generated by Django 3.0.2 on 2020-03-29 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_diagnostic_values'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagnostic',
            old_name='result',
            new_name='diagnosis',
        ),
    ]
