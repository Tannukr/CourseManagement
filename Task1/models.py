from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Make the email field required with a unique constraint
    email = models.EmailField(unique=True)
    # Add role field back with default value
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Faculty', 'Faculty'),
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='Student')
    
    def __str__(self):
        return self.username

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField(default=3)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.course_name
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.user.username