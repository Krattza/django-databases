from django.shortcuts import render
from .models import Student
# Create your views here.
def student_list(request):

    post = Student.objects.all()
    shaina = post[0].firstname
    shaina_teacher = post[0].teacher

    return render(request, 'student/output.html', {
        'post' : post,
        'shaina' :  shaina,
        'shaina_teacher': shaina_teacher
    })
