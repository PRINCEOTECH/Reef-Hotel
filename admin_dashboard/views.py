from django.shortcuts import render


def admin(request):
    return render(request, 'admin_dashboard/base.html')

# Create your views here.
