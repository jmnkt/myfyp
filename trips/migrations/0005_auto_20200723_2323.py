# Generated by Django 3.0.8 on 2020-07-23 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0004_auto_20200723_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending for Acception'), ('ACCEPTED', 'Accepted by Guides'), ('REJECTED', 'Rejected by Guides'), ('IN PROGRESS', 'Planning/Guiding In Progress'), ('COMPLETED', 'Planning/Guiding Completed')], default='PENDING', max_length=32),
        ),
        migrations.AlterField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
