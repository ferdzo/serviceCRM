from django.db import models
from django.contrib.auth.models import UserManager


class Insert(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    note= models.CharField(max_length=100, default=None, blank=True, null=True)
    date = models.DateField("date submitted")
    done = models.BooleanField(default=False)
    repair = models.CharField(default=None, blank=True, null=True,max_length=300)
    plateno = models.CharField(max_length=10, default=None, blank=True, null=True)

    def __str__(self):
        return "Ime: " + self.name + " Telefonski broj: " + self.phone + "\nDefekt: " + self.description + "\nDatum: \n"

    def isDone(self):
        return self.done
