from django.db import models

class License(models.Model):

    activation_code = models.CharField(max_length=20)
    plan_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    activated_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()

    def __str__(self):
        return self.plan_name