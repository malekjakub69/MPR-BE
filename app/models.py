from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager

# TODO: move each class to a seperate dir
# TODO: remove null=True

class User(AbstractBaseUser):

    class UserRoles(models.TextChoices):
        ADMIN = "ADMIN", _("Administrátor"),
        PROJECT_MANAGER = "PROJECT_MANAGER", _("Projektový manažer"),
        USER = "USER", _("Běžný uživatel")
    
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True)
    role = models.CharField(max_length=64, choices=UserRoles.choices, default=UserRoles.USER)
    last_login = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()


    def __str__(self):
        return self.name + ' ' + self.surname + ', ' + self.role


class RiskCategory(models.Model):
    name = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta(object):
        verbose_name_plural = 'Risk Categories'

    def __str__(self):
        return self.name


class Project(models.Model):

    owner_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    #TODO: status
    #date_begin = models.DateField()
    #date_end = models.DateField()

    def __str__(self):
        return self.name