
from django.urls import path   #imported from urls.py original
from . import views  #added import views from current directory
#from django.contrib.auth import views as auth_views #for authentication purpose (login, logout)


urlpatterns = [
    path('syllabus/', views.syllabus, name='syllabus'), 
    path('que-papers/', views.que_papers, name='que-papers'),  
    path('que-papers/<str:sub_name>/<int:sub_id>', views.que_papers_dis, name='que-papers-dis'), 
    
]