from django.shortcuts import render, redirect

from django.contrib import messages

from forum.models import *  #for student table from db

from forum.views import Auth   #authentication forum->views.py->Auth class


def syllabus(request):
    if Auth.auth(request):
        return render(request, 'study/syllabus.html')
    else:
        messages.warning(request, f'Login First')
        return redirect('student-login')

def que_papers(request):
    if Auth.auth(request):
        
        try:
            id = request.session['user-id']
            user = Student.objects.get(stud_id=id)
            year = user.year
            div = user.div_field
            
          

            sub_sem1 = Subjects.objects.raw("SELECT * FROM subjects WHERE year={} and sem = 1 ".format(year))
            sub_sem2 = Subjects.objects.raw("SELECT * FROM subjects WHERE year={} and sem = 2 ".format(year))

            

        except Exception as e:
            sub = {e}

        return render(request, 'study/que.html', {'subjects1':sub_sem1, 'subjects2':sub_sem2})
    else:
        messages.warning(request, f'Login First')
        return redirect('student-login')


def que_papers_dis(request,sub_name, sub_id):
    if Auth.auth(request):
        

        que_papers = QuestionPapers.objects.raw("SELECT * FROM question_papers WHERE subject_id = {} ORDER BY que_year".format(sub_id))
        
        id = request.session['user-id']
        user = Student.objects.get(stud_id=id)
        year = user.year
        
        link = "http://clglyf.epizy.com/1/cse/"
        if year == 2:
            link += "SY/"
        elif year == 3:
            link += "TE/"
        else:
            link += "BE/"
        return render(request, 'study/que.html', {'sub_id':que_papers,'subject_name':sub_name,'link':link })
    else:
        messages.warning(request, f'Login First')
        return redirect('student-login')