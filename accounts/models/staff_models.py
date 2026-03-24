from django.db import models

#  Role Model 
class StaffRole(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


#  Staff Model
class Staff(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    role = models.ForeignKey(StaffRole, on_delete=models.SET_NULL, null=True)

    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()

    photo = models.ImageField(upload_to='staff/', null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

 
# ATTENDANCE MODEL
 

class StaffAttendance(models.Model):

    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    )

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    remark = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('staff', 'date')  

    def __str__(self):
        return f"{self.staff.name} - {self.date} - {self.status}"



# LEAVE MODEL


class StaffLeave(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    from_date = models.DateField()
    to_date = models.DateField()

    reason = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff.name} - {self.status}"