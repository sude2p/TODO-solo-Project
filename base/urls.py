from django.urls import path
from .views import *

urlpatterns =[
    path('home/',home,name='home'),
    path('createTask/', createTask, name='createTask'),
    path('viewTask/<int:pk>/', viewTask, name='viewTask'),
    path('updateTask/<int:pk>/', updateTask, name='updateTask'),
    path('deleteTask/<int:pk>', deleteTask, name='deleteTask')
    
]