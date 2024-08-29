from django.db import models

# Create your models here.

# lass teacher(models.Model):
#  last_name =  models.CharField(max_length=30)
#  first_name = models.CharField(max_length=4 )
#  city = models.CharField(max_length=100 )
#  telephon= models.CharField(max_length=15)
#  cours_suivant= models.CharField(max_length=100,  null=True)
#  vacant= models.CharField(max_length=30, null=True)
class Teacher(models.Model):
    GENDER_CHOICES = (
        ('h','Homme'),
        ('f','Femme'),
    )
    MATTIER_CHOICES = (
        ('Math','Math'),
        ('Physique','Physique'),
        ('EPS','EPS'),
        ('Anglais','Anglais'),
        ('SVT','SVT'),
        ('Philosophie','Philosophie'),
        ('Français','Français'),)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, )
    birth_date = models.DateField()
    matiere = models.CharField(choices=MATTIER_CHOICES, max_length=15)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    vacant= models.CharField(max_length=30)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
    
    def __str__(self):
        return self.first_name
        
        
        
        
        
        
        
      