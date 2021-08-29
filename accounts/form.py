from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=['address' , 'zipcode'] #입력 받을 값!