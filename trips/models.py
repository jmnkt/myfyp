from django.db import models
from profiles.models import Travelers, guideProfile
from country.models import Country, State
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.

class Trip (models.Model):
    tripID = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    countryID = models.ForeignKey('country.Country', on_delete = models.SET_DEFAULT, default = 0000)
    stateID = models.ForeignKey('country.State', on_delete = models.SET_DEFAULT, default = 0000)
    tripStartDate = models.DateField()
    tripEndDate = models.DateField()
    numOfPeople = models.IntegerField()
   
    def __str__(self):
        return str(self.tripID)
   
class tripGuide(models.Model):
   tripID = models.OneToOneField('Trip', on_delete = models.CASCADE)
   guides = models.OneToOneField('profiles.guideProfile', on_delete = models.SET_DEFAULT, default = 0000, null = True, blank = True)
   statusChoices = [
       ('PENDING','Pending for Acception'),
       ('ACCEPTED', 'Accepted by Guides'),
       ('REJECTED', 'Rejected by Guides'),
       ('IN PROGRESS', 'Planning/Guiding In Progress'),
       ('COMPLETED', 'Planning/Guiding Completed'),
    ]
   status = models.CharField(
       max_length=32,
       choices=statusChoices,
       default='PENDING',
   )


