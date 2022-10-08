from django.shortcuts import render
from .forms import UserUpdateForm, ProfileUpdateForm



def Profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'customer/profile.html', context)

# Create your views here.
