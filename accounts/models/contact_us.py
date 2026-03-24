from django.db import models

class SchoolMap(models.Model):

    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map_embed = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.address


class ContactMessage(models.Model):

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    is_read = models.BooleanField(default=False)   # 👈 add this

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name