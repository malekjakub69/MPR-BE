from django.db import models
from .choices import UserRoles

# Class User
class User(models.Model):    
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    role = models.CharField(max_length=64, choices=UserRoles.choices, default=UserRoles.USER)

    def __str__(self):
        return self.name + ' ' + self.surname + ', ' + self.role