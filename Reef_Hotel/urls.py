
from django.contrib import admin
from django.urls import path, include
from registration import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
    path('register/', user_views.RegisterUser, name='register'),
    path('login/', user_views.LoginUser, name='login'),
    path('logout/', user_views.LogoutUser, name='logout'),
    path('', include('booking.urls')),
    path('', include('customer.urls')),
    path('', include('admin_dashboard.urls')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
