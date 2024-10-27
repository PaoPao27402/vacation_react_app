from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

# No need to register `User` here if it's already registered by Django.
