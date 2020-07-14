from django import forms
from .models import User, Guides

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'gender',
            'passportNo',
            'email',
            'address',
            'dateOfBirth',
            'profilePic'   
        ]

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guides
        fields = [
            'guidingCountry',
            'licenses',
            'itinerary',
            'introduction'
        ]