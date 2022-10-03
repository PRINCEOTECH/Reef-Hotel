from django.shortcuts import render



def Profile(request):
    return render(request, 'customer/profile.html')

# Create your views here.
