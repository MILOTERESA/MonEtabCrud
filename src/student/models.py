from django.db import models

# Create your models here.
class Student(models.Model):
      GENDER_CHOICES = (
            ('h','Homme'),
            ('f','Femme'),
      )
      CLASSE_CHOICES = (
            ('terminale','terminale'),
            ('premier','premier'),
            ('second','second'),
            ('troisieme','troisieme'),
            ('quatrieme','quatrieme'),
            ('cinquieme','cinquieme'),
      )
      first_name = models.CharField(max_length=30)
      last_name =  models.CharField(max_length=30)
      Genre = models.CharField(max_length=30, choices=GENDER_CHOICES)
      registration_number = models.CharField(max_length= 20 , null =True )
      birth_date = models.DateField()
      Classe= models.CharField(max_length=15, choices=CLASSE_CHOICES)
      phone_number=models.CharField(max_length=30)
      city=models.CharField(max_length=30)
      
      class Meta:
            verbose_name = 'student'
            verbose_name_plural = 'students'
      
      
