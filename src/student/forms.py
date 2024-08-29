from django import forms
from .models import Student 

# class StudentForm(forms.Form):
#       first_name = forms.CharField(max_length=30)
#       last_name =  forms.CharField(max_length=30)
#       genre = forms.CharField(max_length=4)
#       registration_number = forms.CharField(max_length= 20)
#       Date_Naissance = forms.DateField()
#       classe= forms.CharField(max_length=10,)
#       ville= forms.CharField(max_length=30,)
      
class StudentForm(forms.ModelForm):
      class Meta:
            model = Student
            fields = "__all__"
            widgets = {
            'genre': forms.RadioSelect,
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
      }

      
