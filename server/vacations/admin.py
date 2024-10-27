from django.contrib import admin
from .models import Country, Vacation, UserStatistics

admin.site.register(Country)
admin.site.register(Vacation)
admin.site.register(UserStatistics)
