from django.db import models
from django.contrib.auth.models import User 
from myuser.models import Myuser
# Create your models here.

#class UserProfile(User):
 #   Faculty_type=models.CharField(max_length=3, choices=CATEGORIES)
  #
   # def __str__(self):
    #    return self.username+self.Login_type


class Course(models.Model):
    course_id=models.CharField(max_length=5, primary_key=True)
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.pk)
    
class Student(models.Model):
    roll_no=models.IntegerField(max_length=9)
    name=models.CharField(max_length=50)
    courses=models.ManyToManyField(Course, limit_choices_to=6)
    
    def __str__(self):
        return str(self.pk)
    

class Attendance(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    date=models.DateField()
    user=models.ForeignKey(Myuser, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.pk)
    