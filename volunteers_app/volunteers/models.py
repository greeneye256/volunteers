from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % self.name


class Volunteer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.date_of_birth.__str__())


