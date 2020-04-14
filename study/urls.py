
from django.urls import path   #imported from urls.py original
from . import views  #added import views from current directory
#from django.contrib.auth import views as auth_views #for authentication purpose (login, logout)


urlpatterns = [
    path('syllabus/', views.syllabus, name='syllabus'),  
    
]