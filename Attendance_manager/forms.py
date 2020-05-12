from .models import *
from django import forms

class Student(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_no', 'name', 'courses']
        
class Course(forms.ModelForm):
    class Meta:
        model = Course
        fields=['course_id', 'name']

        
class Attendance(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'course', 'date']
        exclude=('user,')