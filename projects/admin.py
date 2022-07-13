from django.contrib import admin
# Register your models here.

from .models import Project, Review, Tag
# Add Project class from models.py into the database
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
