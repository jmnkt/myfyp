# Generated by Django 3.0.8 on 2020-07-23 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20200723_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='status',
        ),
        migrations.AddField(
            model_name='tripguide',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending for Acception'), ('ACCEPTED', 'Accepted by Guides'), ('REJECTED', 'Rejected by Guides'), ('IN PROGRESS', 'Planning/Guiding In Progress'), ('COMPLETED', 'Planning/Guiding Completed')], default='PENDING', max_length=32),
        ),
    ]