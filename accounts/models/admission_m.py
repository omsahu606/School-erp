from django.db import models

class AdmissionApplication(models.Model):

    student_name = models.CharField(max_length=200)
    dob = models.DateField()
    applying_class = models.CharField(max_length=50)

    parent_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

 
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected')
        ],
        default='pending'
    )

    def __str__(self):
        return self.student_name
    
    
