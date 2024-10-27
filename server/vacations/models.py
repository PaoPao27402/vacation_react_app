from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vacation(models.Model):
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    likes = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)  # Link to Country

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

class UserStatistics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User
    total_vacations = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.email} Statistics"
