from django.db import models

class Country(models.Model):
    countryCode = models.CharField(primary_key = True, max_length = 100)
    countryName = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.countryName
    
class State(models.Model):
    country = models.ForeignKey('Country', on_delete = models.CASCADE)
    stateCode = models.CharField(primary_key = True, max_length = 100)
    stateName = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.stateCode