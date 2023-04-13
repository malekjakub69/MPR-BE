from django.db import models

class User(models.Model):
    password = models.BinaryField(max_length=256)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    USER_ROLES = [
        ("ADMIN", "Administrátor"),
        ("PROJECT_MANAGER", "Projektový manažer"),
        ("USER", "Běžný uživatel"),
    ]
    role = models.CharField(max_length=64, choices=USER_ROLES)
