from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Vacation(models.Model):
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.destination} - {self.price}"

class UserStatistics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vacation_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.vacation_count} vacations"
