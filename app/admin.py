from django.contrib import admin
from .models import User, RiskCategory, Project

admin.site.register(User)
admin.site.register(RiskCategory)
admin.site.register(Project)

# you can create a superuser who has administrative access to the database: http://localhost:8000/admin