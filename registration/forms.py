from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django_countries.fields import CountryField






class CreateUserForm(UserCreationForm):
    Email = forms.EmailField(required=True)
    First_Name = forms.CharField(max_length= 200, required=True)
    Last_Name = forms.CharField(max_length= 200, required=True)
    Address = forms.CharField(max_length=200, required=True)
    Bio = forms.CharField(max_length=500, label="bio", required=True)
    Country = CountryField(blank_label='(select country)').formfield()
    State = forms.CharField(max_length=300, required=True)
    City = forms.CharField(widget=forms.TextInput(), max_length=50, label="city", required=True)
    Zip = forms.IntegerField(label="zip", required=True)
    Phone_Number = forms.IntegerField(required=True)
    
    class Meta:
        model = User
        fields = ["First_Name", "Last_Name","username", "Bio", "Country", "State", "City", "Address", "Zip", "Phone_Number", "Email", "password1", "password2"]