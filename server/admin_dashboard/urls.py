# admin_dashboard/urls.py
from django.contrib import admin
from django.urls import path, include
from vacations.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vacations.urls')),
    path('api/users/', include('users.urls')),  
    path('', HomeView.as_view(), name='home'),
]
