from django.shortcuts import render, redirect
from django.contrib import messages

#from django.http import HttpResponse  #added
from .models import Forum, Student, ForumReplies    


from student.views import Auth          # student->view.py->Auth(class)   to verify user
# Create your views here.


#to authenticate data from create new forum 
class authForum:
    def __init__(self, name, desc, due):
        self.name = name
        self.desc = desc
        self.due = due

    def authForum(self,request):
        global messages
        self.name = str(self.name).strip()
        if len(self.name):      # forum name is empty or not
            if len(self.desc):  #same for desc
                if len(self.due):
                    id = request.session['user-id']     #id of user from session which mathches to id from student table
                    Forum.objects.create(user_id=id, forum_name=self.name, description=self.desc, due_date=self.due,reply=0,status=0)  #uhh add data to forum table
                    return True
                else:
                    messages.warning(request, f'Due date can\'t be empty')  #messages is inbuild module to throw warnings or success or anything
            else:
                messages.warning(request, f'Forum description can\'t be empty')
        else:
            messages.warning(request, f'Forum name can\'t be empty')



def index(request):
    if Auth.auth(request):              #imported class to auth user
        if request.method == "POST":    
            global messages
            data = request.POST.copy()
            name = data.get('forum-name')
            desc = data.get('create-forum')
            due = data.get('due')
            
            newForum = authForum(name,desc,due)
            message = newForum.authForum(request)
            if message == True:
                messages.success(request, f'Successfully posted')
            else:
                messages = message
            
            return redirect( 'forum-home')
        #forum data
        try:
            id = request.session['user-id']

            #user = Users.objects.get(user_id = id)
            from django.db import connection
            cursor = connection.cursor()    
            cursor.execute("SELECT forum_id,user_id,fname,lname,forum_name,description,date_post,reply FROM forum INNER JOIN student ON forum.user_id = student.stud_id WHERE status=0 ORDER BY forum_id DESC")
            forums = cursor.fetchall()
        
            return render(request, 'forum/index.html',{'forum':forums})
        except Exception as e :
            messages.warning(request, f'No posts{e}')
            return render(request, 'forum/index.html',{'forum':None})
            

    else:       #failed auth . return back to login page with message
        messages.warning(request, f'Login First')
        return redirect('student-login')

        
    

def viewDisscussion(request,forum_id):
    if Auth.auth(request):
        id = request.session['user-id']

        if request.method == "POST":
            data = request.POST.copy()
            reply = data.get("reply")
            reply = reply.strip()
            if len(reply):
                try:
                    ForumReplies.objects.create(forum_id=forum_id,user_id=id,reply=reply,status=0)
                    messages.warning(request, f'Posted...')
                except:
                    messages.warning(request, f'Something went wrong!!')
            else:
                messages.warning(request, f'Please write something')
        #forums = Forum.objects.filter(status=0,forum_id=forum_id).prefetch_related()

        from django.db import connection
        cursor = connection.cursor()    
        cursor.execute("SELECT forum_id,user_id,fname,lname,forum_name,description,date_post FROM forum INNER JOIN student ON forum.user_id = student.stud_id WHERE forum_id={}".format(forum_id))
        forums = cursor.fetchall()   #fetch forum
        
        
        cursor.execute("SELECT reply_id,user_id,fname,lname,reply,posted_date FROM forum_replies INNER JOIN student ON user_id=stud_id WHERE status=0 and forum_id={} ORDER BY reply_id DESC ".format(forum_id))
        replies = cursor.fetchall()   #fetch all replies of that forum

        return render(request, 'forum/view-diss.html',{'forum':forums,'reply':replies})
    else:
        messages.warning(request, f'Login First')
        return redirect('student-login')
