from django.urls import path
from .views import index,update,add,delete

app_name='teacher'

urlpatterns = [
path('', index,name="teacher"),
path('add/',add,name="add_teacher"),
path('update/<int:id>/', update, name = 'update'),
path('delete/<int:id>/', delete, name = 'delete')
]

