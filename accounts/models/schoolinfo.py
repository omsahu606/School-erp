from django.db import models

class SchoolSettingsinfo(models.Model):

    school_name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField(default="Ripur CG" ,null=True, blank=True)
    logo = models.ImageField(upload_to='school_logo/', null=True, blank=True)

    def __str__(self):
        return self.school_name