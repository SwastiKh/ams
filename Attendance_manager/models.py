from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.pk)
    
class Course(models.Model):
    course_id=models.CharField(max_length=5, primary_key=True)
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.pk)
    
class Attendance(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    couurse=models.ForeignKey(Course, on_delete=models.CASCADE)
    date=models.DateField()
        
    def __str__(self):
        return str(self.pk)
    