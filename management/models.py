from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class AdminUser(AbstractUser):
    ROLE_TYPES = (
        ('ADMIN', 'ADMIN'),
        ('EMPLOYEE', 'EMPLOYEE'),
    )

    role = models.CharField(max_length=10, choices=ROLE_TYPES)

    def __str__(self):
        return self.username
    

class Employee(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    emp_start_date = models.DateField()
    emp_end_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name