from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
import traceback
from .models import Student
from .form import StudentForm

# Create your views here.

from .models import Student

def listStudent(request):
    student_list = Student.objects.all()

    context ={
        'student_list':student_list,
    }
    return render(request, 'students/list_student.html', context)

def addStudent(request, studentId):    
    errorList = []
    form = StudentForm()
    if request.method == 'POST':
        try:
            form = StudentForm(request)
            errorList = form.validate()

            if not errorList:
                form.save()
                return redirect('list_student')
            
        except Exception as e:
            traceback.print_exc()
            errorList.append(str(e))
    
    elif studentId > 0:
        student = get_object_or_404(Student,pk=studentId)
        form =StudentForm(dbModel=student)
    
    context = {
        'form' : form, 
        'errorList' : errorList,
    }

    return render(request, 'students/add_edit_student.html', context)

def deleteStudent(request, studentId):
    student = get_object_or_404(Student, pk=studentId)
    student.delete()
    return redirect('students/list_student')