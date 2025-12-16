from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('STUDENT', 'Student'),
        ('LIBRARIAN', 'Librarian'), 
        ('ADMIN', 'Admin'),
    ]                                   
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='STUDENT')

    def __str__(self):
        return f'{self.username} - {self.role}'
    
    def is_student(self):
        return self.role == 'STUDENT'
    
    def is_librarian(self):
        return self.role == 'LIBRARIAN'
    
    def is_admin(self):
        return self.role == 'ADMIN'
    
# Create your models here.
