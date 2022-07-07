from django import forms
from .models import Restuarant, Cuisines, Menu

class ResForm(forms.ModelForm):
    
    class Meta:
        model = Restuarant
        fields = [
            'name',
            'discriptions',
            'location',
            'cuisines',
            'veg_type',
            'rating',
            'contact',
            'email'
        ]

class CuisForm(forms.ModelForm):
    class Meta:
        model = Cuisines
        fields = [
            'cuisines_type'
        ]

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            'name',
            'description',
            'cuisines_type',
            'price',
            'veg_type',
            'rname'
        ]