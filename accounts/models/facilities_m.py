from django.db import models


class Facility(models.Model):

    name = models.CharField(max_length=200)
    features = models.TextField()
    image = models.ImageField(upload_to='facilities/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name