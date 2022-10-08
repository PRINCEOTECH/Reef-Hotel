from django.urls import path
from .views import admin




urlpatterns = [
    path('reef/', admin, name='admin')
]