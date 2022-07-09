from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # Go into projects folder and include urls.py in that folder.
    path('', include('projects.urls'))
]
