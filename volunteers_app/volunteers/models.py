from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=20)




class Volunteer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
