from django.db import models
class EmployeeData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.BigIntegerField()
    company = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=50)
    home_town = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    skill = models.CharField(max_length=50)
    percentage = models.IntegerField()
