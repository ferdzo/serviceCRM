from django.db import models
from django.contrib.auth.models import UserManager


class Insert(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    date = models.DateField("date submitted")
    done = models.BooleanField()

    def __str__(self):
        return "Ime: " + self.name + " Telefonski broj: " + self.phone + "\nDefekt: " + self.description + "\nDatum: \n"

    def isDone(self):
        return self.done
