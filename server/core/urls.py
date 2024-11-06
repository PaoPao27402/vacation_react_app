from django.urls import path
from . import views

urlpatterns = [
    # URL for getting all vacations
    path("vacations/", views.get_vacations, name='get_vacations'),

    # Uncomment to enable the route for getting all vacations
    # path("all_vacations/", views.get_all_vacations, name='get_all_vacations'),

    # URL for getting likes
    path("likes/", views.get_likes, name='get_likes'),

    # URL for getting users
    path("users/", views.get_users, name='get_users'),

    # URL for getting countries
    path("countries/", views.get_countries, name='get_countries'),

    # URL for login
    path('login/', views.login, name='login'),
]
