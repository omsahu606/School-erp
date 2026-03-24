from django.db import models

class AboutUs(models.Model):
    #  School Basic Info
    about_text = models.TextField()
    location = models.CharField(max_length=255)
    email = models.EmailField(default="admin@example.com")

    #  Management Section
    management_name = models.CharField(max_length=150)
    management_title = models.CharField(max_length=150)
    management_message = models.TextField()
    management_photo = models.ImageField(upload_to='management/')

    #  Principal Section
    principal_name = models.CharField(max_length=150)
    principal_title = models.CharField(max_length=150)
    principal_message = models.TextField()
    principal_photo = models.ImageField(upload_to='principal/')

    def __str__(self):
        return "About Page"