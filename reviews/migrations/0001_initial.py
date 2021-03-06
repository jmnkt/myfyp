# Generated by Django 3.0.8 on 2020-07-14 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('profiles', '0004_auto_20200715_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='guideReviews',
            fields=[
                ('reviewID', models.AutoField(primary_key=True, serialize=False)),
                ('reviewContent', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='travelerReviews',
            fields=[
                ('reviewID', models.AutoField(primary_key=True, serialize=False)),
                ('reviewContent', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1)),
                ('GuideID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='profiles.Guides')),
                ('senderID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='profiles.Travelers')),
            ],
        ),
    ]
