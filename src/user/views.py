from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserForm
from . models import User

# Create your views here.
def index(request):
    users = User.objects.all() 
    context= {"users":users}
    return render(request,"user/user.html",context)
    

def add(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:user')
    else:
        user_form = UserForm()        
    return render(request ,"user/add_user.html",{"user_form":user_form})
    
    
def update (request,id):
    user = User.objects.get(id=id)
    if request.method =='POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            messages.success (request,"lutilisateur a éte modifie avec succes")
            return redirect('user:user')
        else:
            messages.error(request, "Erreur lors de modification de l'utilsateur. Vueillez corriger le formulaire")
            return render(request,'user/add_user.html',{'user_form': user_form})
            
    user_form = UserForm(instance=user)
    
    
    context = {
        'user_form': user_form,
        'title':"Modifier utilisateur"
    }
    return render (request, 'user/add_user.html',context)
    
    

def delete(request, id): 
     user = User.objects.get(id=id)
     user.delete()
     messages.success(request, "L'élève a été supprimé avec succés.")
     return redirect('user:index')
        
        

    

