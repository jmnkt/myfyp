# Generated by Django 3.0.8 on 2020-07-23 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='countryCode',
            new_name='country',
        ),
    ]
