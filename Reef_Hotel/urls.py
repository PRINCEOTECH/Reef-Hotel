
from django.contrib import admin
from django.urls import path, include
from registration import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
    path('register/', user_views.RegisterUser, name='register'),
    path('login/', user_views.LoginUser, name='login'),
    path('logout/', user_views.LogoutUser, name='logout'),

    path('', include('booking.urls')),

    path('', include('customer.urls')),
    
]
