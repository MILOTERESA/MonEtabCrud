from django import forms
from .models import User

class UsersForm(forms.Form):
    pseudo = forms.CharField(max_length=25)
    mot_de_passe = forms.CharField(max_length=25)
    creat_at = forms.CharField()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["created_at"]
   
   

