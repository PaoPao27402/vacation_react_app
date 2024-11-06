# users/urls.py
from django.urls import path
from .views import UserRegistrationView, LoginView, ProtectedView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected_view'),
]