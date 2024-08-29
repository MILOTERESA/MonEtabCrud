from django.urls import path
from .views import index, add_student, update,delete

app_name='student'

urlpatterns = [
path('', index, name = 'student'),
path('add/', add_student, name = 'add_student'),
path('update/<int:id>/', update, name = 'update'),
path('delete/<int:id>/', delete, name = 'delete')
]

