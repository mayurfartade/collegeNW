
from django.urls import path   #imported from urls.py original
from . import views  #added import views from current directory
#from django.contrib.auth import views as auth_views #for authentication purpose (login, logout)


urlpatterns = [
    
    path('login/', views.login, name='student-login'),  #empty path means nothing passed through url, views.index means index function in views file
    path('register/', views.register, name='student-register'),
    path('register-extra/', views.register_extra, name='student-extra-register'),
    path('home/', views.home, name='student-home'),
    path('logout/', views.logout, name='student-logout'),


]