# Django Takeaways

In DIRS of TEMPLATES in settings.py, set file path ->
os.path.join(BASE_DIR, ‘templates’): BASE_DIR points to the root directory, look for the file named ‘templates’

views.py example
def func(request):
	return render (request, ‘projects.html’)

Template Inheritance
Way to include template into another template
{% include ‘abc.html’ %}

Way to integrate multiple templates into the main template so that they share the ‘main’ template
{% extends ‘main.html’ %}
