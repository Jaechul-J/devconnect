from django.contrib import admin
# Register your models here.

from .models import Project
admin.site.register(Project) # Add Project class from models.py into the database