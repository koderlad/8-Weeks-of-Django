from django.contrib import admin
from .models import Candidate

# Register your models here. This allows to control the models via Django's built-in admin interface
admin.site.register(Candidate)