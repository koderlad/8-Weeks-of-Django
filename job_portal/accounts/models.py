from django.contrib.auth.models import User #Importing the built in django user model
from django.db import models

#User Model
class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('candidate', 'Candidate'),
        ('employer', 'Employer') #Tuples
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username

#Employer models
class Employer(models.Model):
    company_name = models.CharField(max_length=200)
    contact_email = models.EmailField(unique=True)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=200, blank=True, null=True)

    def __self__(self):
        return self.company_name

#Candidate Model
class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # A String representation for the admin panel and debugging.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

