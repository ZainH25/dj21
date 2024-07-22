from .models import Student
from django import forms
from .models import Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'course_id']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'email'] 