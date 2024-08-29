from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TeacherForm
from .models import Teacher

# Create your views here.
def index(request):
    teachers= Teacher.objects.all()
    context= {"teachers":teachers}
    return render(request, "teacher/teacher.html",context)
    
    
    
def update (request,id):
    teacher = Teacher.objects.get(id=id)
    if request.method =='POST':
        teacher_form = TeacherForm(request.POST, instance=teacher)
        if  teacher_form.is_valid():
            teacher_form.save()
            messages.success (request,"le professeur a éte modifie avec succes")
            return redirect('teacher:teacher')
        else:
            messages.error(request, "Erreur lors de modification de le professeur. Vueillez corriger le formulaire")
            return render(request,'teacher/add_teacher.html',{ 'teacher_form': teacher_form})
            
    teacher_form = TeacherForm(instance=teacher)
    
    
    context = {
        'teacher_form': teacher_form,
        'title':"Modifier utilisateur"
    }
    return render (request, 'teacher/add_teacher.html',context)
    
def add(request):
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect('teacher:teacher')
    else:
        teacher_form = TeacherForm()
    return render(request, "teacher/add_teacher.html", {'teacher_form': teacher_form })
    
    
def delete (request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    messages.success(request, "Le professeur à été supprimé avec succès")
    return redirect('teacher:teacher')
    
    
    