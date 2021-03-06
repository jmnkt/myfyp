# Generated by Django 3.0.8 on 2020-07-23 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0019_remove_guideprofile_userprofiles'),
        ('trips', '0003_auto_20200723_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='guidesID',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='travelerID',
        ),
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='tripGuide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guides', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='profiles.guideProfile')),
                ('tripID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip')),
            ],
        ),
    ]
