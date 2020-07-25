from django import forms
from .models import messageToGuide, messageToTraveler

class messageToGuideForm(forms.ModelForm):
    class Meta:
        model = messageToGuide
        fields = [
        'content'
        ]
        
class messageToTravelerForm(forms.ModelForm):
    class Meta:
        model = messageToTraveler
        fields = [
        'content'
        ]