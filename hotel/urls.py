from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('hotel/', views.hotel, name='hotel'),
]
