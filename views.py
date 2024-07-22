from .forms import StudentForm, CourseForm
from .models import Student, Course
from django.shortcuts import render, redirect, get_object_or_404
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
# Redirect to a view that lists all students
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'course_registration/add_student.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_registration')
    else:
        form = CourseForm()
    return render(request, 'course_registration/add_course.html', {'form': form})

def register_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        course_id = request.POST.get('course_id')

        if not student_name or not course_id:
            return render(request, 'course_registration/register_student.html',{'courses': Course.objects.all(),'error_message': 'Please provide both student name and select a course.'})
        try:

            course = get_object_or_404(Course, pk=course_id)

            student = Student.objects.filter(name=student_name).first()
            if not student:

                return render(request, 'course_registration/register_student.html',{'courses': Course.objects.all(), 'error_message': 'Student does not exist in the database.'})

            course.students.add(student)
            return redirect('course_registration')
        except Course.DoesNotExist:
            return render(request, 'course_registration/register_student.html',{'courses': Course.objects.all(), 'error_message': 'Invalid course ID. Please select a valid course.'})

    return render(request, 'course_registration/register_student.html', {'courses': Course.objects.all()}) 

def course_registration(request):
    courses = Course.objects.all()
    return render(request, 'course_registration/course_registration.html.html',{'courses': courses})

def students_list(request, course_id):

    course = get_object_or_404(Course, course_id=course_id)

    students = course.students.all()
    return render(request, 'course_registration/students_list.html', {'course': course, 'students': students})
    