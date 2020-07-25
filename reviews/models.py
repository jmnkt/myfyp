from django.db import models
from profiles.models import userProfile
from trips.models import Trip
from django.contrib.auth import get_user_model

User = get_user_model()

class ReviewsForGuides(models.Model):
    reviewID = models.AutoField(primary_key = True)
    recipientID = models.IntegerField()
    senderID = models.ForeignKey(User, on_delete=models.CASCADE)
    tripID = models.IntegerField()
    reviewContent = models.TextField()
    ratingChoices = [
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ]
    rating = models.IntegerField(choices = ratingChoices, default = 1)

class ReviewsForTravelers(models.Model):
    reviewID = models.AutoField(primary_key = True)
    recipientID = models.IntegerField()
    senderID = models.ForeignKey(User, on_delete=models.CASCADE)
    tripID = models.IntegerField()
    reviewContent = models.TextField()
    ratingChoices = [
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ]
    rating = models.IntegerField(choices = ratingChoices, default = 1)
