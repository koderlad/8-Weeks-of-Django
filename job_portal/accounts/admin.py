from django.contrib import admin
from .models import Candidate, Employer

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_email', 'location')
    search_fields = ('company_name', 'contact_email')


# Register your models here. This allows to control the models via Django's built-in admin interface
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Employer, EmployerAdmin)