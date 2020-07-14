from django.db import models

# Create your models here.
class Trip (models.Model):
    tripID = models.AutoField(primary_key = True)
    travelerID = models.ForeignKey('Travelers', on_delete = models.SET_NULL)
    guidesID = models.ForeignKey('Guides', on_delete = models.SET_NULL)
    countryID = models.ForeignKey('Country', on_delete = models.SET_NULL)
    stateID = models.ForeignKey('State', on_delete = models.SET_NULL)
    tripDate = models.DateField()
    numOfPeople = models.IntegerField()



