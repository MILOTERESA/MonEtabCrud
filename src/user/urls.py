from django.urls import path
from .views import index,update,add,delete

app_name='user'

urlpatterns = [
path('', index, name = 'user'),
path('add',add,name="add_user"),
path('update/<int:id>', update, name = 'update'),
path('delete/<int:id>', delete, name = 'delete')
]


