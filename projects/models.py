from django.db import models
import uuid
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)  # Required field
    description = models.TextField(null=True, blank=True)  # Not a required field
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title # Make each project name appear as title not 'Project object'