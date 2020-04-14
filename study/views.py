from django.shortcuts import render, redirect

from django.contrib import messages

from forum.models import Student  #for student table from db

from forum.views import Auth   #authentication forum->views.py->Auth class

def syllabus(request):
    if Auth.auth(request):
        return render(request, 'study/syllabus.html')
    else:
        messages.warning(request, f'Login First')
        return redirect('student-login')