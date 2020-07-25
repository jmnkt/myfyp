from django import forms
from .models import Trip, tripGuide

class tripDetailsForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
           'countryID',
           'stateID',
           'tripStartDate',
           'tripEndDate',
           'numOfPeople',
        ]

class tripGuideForm(forms.ModelForm):
    class Meta:
        model = tripGuide
        fields = [
            'tripID',
            'guides'
        ]
        
class tripGuideFormForGuide(forms.ModelForm):
    class Meta:
        model = tripGuide
        fields = [
            'status',
        ]

