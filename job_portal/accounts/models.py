from django.db import models

# Create your models here.
#Creating Candidate Model
class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resues/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # A String representation for the admin panel and debugging.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

