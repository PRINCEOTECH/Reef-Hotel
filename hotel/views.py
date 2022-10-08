from django.shortcuts import render
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'hotel/index.html')
    

@login_required(login_url='login')
def blog(request):
    return render(request, 'hotel/blog.html')


@login_required(login_url='login')
def contact(request):
    return render(request, 'hotel/contact.html')


@login_required(login_url='login')
def services(request):
    return render(request, 'hotel/services.html')


@login_required(login_url='login')
def hotel(request):
    return render(request, 'hotel/hotel.html')

# Create your views here.
