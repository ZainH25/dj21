from django.contrib import admin
from .models import Student, Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_id']

admin.site.register(Student)
admin.site.register(Course, CourseAdmin)
