from django import forms
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    Email = forms.EmailField()
    First_Name = forms.CharField(max_length= 200)
    Last_Name = forms.CharField(max_length= 200)
    

    class Meta:
        model = User
        fields = ["First_Name", "Last_Name","username", "Email",]

class ProfileUpdateForm(forms.ModelForm):
    Address = forms.CharField(max_length=200)
    Bio = forms.CharField(max_length=500)
    Country = CountryField(blank_label='(select country)').formfield()
    State = forms.CharField(max_length=300)
    City = forms.CharField(widget=forms.TextInput(), max_length=50)
    Zip = forms.IntegerField()
    Phone_Number = forms.IntegerField()
    class Meta:
        model = Profile
        fields = ['image', "Bio", "Country", "State", "City", "Address", "Zip", "Phone_Number"]



