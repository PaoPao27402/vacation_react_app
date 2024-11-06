from django.db import models
from django.forms import ModelForm, DateInput, NumberInput, Select, TextInput, FileInput



class CountryModel(models.Model):
    countryId = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country

    class Meta:
        db_table = "countries"


class RoleModel(models.Model):
    roleId = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=50)

    def __str__(self):
        return self.roleName

    class Meta:
        db_table = "roles"


class UserModel(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    roleId = models.ForeignKey(RoleModel, on_delete=models.CASCADE, db_column='roleId')

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    class Meta: 
        db_table = "users"


class VacationModel(models.Model):
    vacationId = models.AutoField(primary_key=True)
    countryId = models.ForeignKey('CountryModel', on_delete=models.CASCADE, db_column='countryId')
    description = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    VacationPicture = models.ImageField(upload_to='VacationPicture/')

    def __str__(self):
        return f"{self.description} ({self.startDate} - {self.endDate})"
    
    class Meta: 
        db_table = "vacations"


class LikeModel(models.Model):
    likesId = models.AutoField(primary_key=True)
    userID = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_column='userId')
    vacationId = models.ForeignKey(VacationModel, on_delete=models.CASCADE, db_column='vacationId')
    
    def __str__(self):
        return f"Like: {self.userID} - {self.vacationId}"

    class Meta: 
        db_table = "likes"
        unique_together = ('userID', 'vacationId')


class VacationForm(ModelForm):
    class Meta:
        model = VacationModel
        exclude = ["vacationId"]
        widgets = {
            "country": Select(attrs={"class": "form-control"}),
            "description": TextInput(attrs={"class": "form-control", "minlength": 2, "maxlength": 50}),
            "startDate": DateInput(attrs={"class": "form-control", "type": "date"}),
            "endDate": DateInput(attrs={"class": "form-control", "type": "date"}),
            "price": NumberInput(attrs={"class": "form-control", "min": 0, "max": 10000}),
            "vacation_picture": FileInput(attrs={"class": "form-control", "type": "file"}),        }