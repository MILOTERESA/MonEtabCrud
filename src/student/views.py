from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context= {"students":students}
    return render(request,"student/student.html",context)
    
    
def update (request,id):
    student = Student.objects.get(id=id)
    if request.method =='POST':
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            messages.success (request,"L'élève a éte modifié avec succes")
            return redirect('student:student')
        else:
            messages.error(request, "Erreur lors de modification de L'élève. Vueillez corriger le formulaire")
            return render(request,'student/add_student.html',{'stud_form': student_form})
            
    student_form = StudentForm(instance=student)
    
    
    context = {
        'stud_form': student_form,
        'title':"Modifier élève"
    }
    return render (request, 'student/add_student.html',context)
    
    
def add_student(request):
    if request.method == "POST":
        stud_form = StudentForm(request.POST)
        if stud_form.is_valid():
            stud_form.save()
            return redirect('student:student')
    else:
        stud_form = StudentForm()
        
    return render(request,"student/add_student.html",{'stud_form':stud_form})

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, "L 'éleve à été supprimé avec succès")
    return redirect('student:student')
    
