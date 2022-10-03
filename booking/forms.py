from django import forms



class AvailabilityForm(forms.Form):
    
    check_in_date = forms.DateField(required=True, input_formats=['%Y-%m-%d'])
    check_in_time = forms.TimeField(required=True, input_formats=['%H:%M'])
    check_out_date = forms.DateField(required=True, input_formats=['%Y-%m-%d'])
    check_out_time = forms.TimeField(required=True, input_formats=['%H:%M'])
    beds = forms.IntegerField(required=True)
    number_of_occupant = forms.IntegerField(required=True)