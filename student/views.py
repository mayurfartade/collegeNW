
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from forum.models import Student

class Auth:         #auth class to check user is loggedin or not using session variables
    @staticmethod
    def auth(request):
        if request.session.has_key('user-id') and not request.session.has_key('extra'):
        #username = request.session['user-id']
            return True
        return False



#verify data from student signup form
class studentRegistration:
    def __init__(self, email,fname,lname,mono,gender,passwd,cpasswd):
        self.email = email  
        self.fname = str(fname).title()
        self.lname = str(lname).title()
        self.mono = mono 
        self.gender = gender 
        self.passwd = passwd
        self.cpasswd = cpasswd 
    

    #validate extra sign up data after first signup
    @staticmethod
    def auth_extra(request,year,div,roll_no,prn_no,birthday):
        global messages
        if year in ['2','3','4']:   #2,3,4 for 2nd, 3rd,....year
            if div in ['A','B','C']:
                if str(roll_no).isnumeric() and str(prn_no).isnumeric():
                    
                    try:
                        stud_id = request.session['user-id']
                        stud = Student.objects.get(stud_id=stud_id)
                        stud.year = year
                        stud.div_field = div
                        stud.roll_no = roll_no
                        stud.prn_no = prn_no
                        stud.birthday = birthday
                        stud.branch = 1
                        stud.save()
                        del request.session['extra']
                        return True
                    except:
                        messages.warning(request, f'Something weng wrong')

                else:
                    messages.warning(request, f'Roll no or PRN no is not correct')
            else:
                messages.warning(request, f'Div is incorrect')
        else:
            messages.warning(request, f'Year is incorrect')
        return messages

    #first signup data validation
    def auth(self,request):
        global messages
        import re
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if(re.search(regex,self.email)):
            if str(self.fname).isalpha() and str(self.lname).isalpha():
                if len(str(self.mono)) == 10:
                    if self.passwd == self.cpasswd:
                        if len(str(self.passwd)) > 5:
                            try:
                                user = Student.objects.get(email=self.email)  #fetch email from db if found then dispaly error else add to db
                                messages.warning(request, f'Email is already taken!!{user.email}')
                                return redirect('student-register')
                            except:     
                                Student.objects.create(email=self.email,password=self.passwd,fname=self.fname,lname=self.lname, mobile=self.mono, gender=self.gender,branch=0,year=0)
                                return True
                        else:
                            messages.warning(request, f'Password must be greater than 6 Characters.')
                    else:
                        messages.warning(request, f'Password and Retype password are not same')
                else:
                    messages.warning(request, f'Mobile number is not correct')
            else:
                messages.warning(request, f'First of Last name is not correct')
        else:
            messages.warning(request, f'Email is not correct')
        return messages



def login(request):
    global messages
    if Auth.auth(request):  #if user is already logged in then redirect to home page
        #username = request.session['user-id']
        messages.success(request, f'Logout to login')
        return redirect('student-home')

    elif request.method == "POST":          #login request
        data = request.POST.copy()
        email = data.get('email')           #html input names
        passwd = data.get('password')
        try:
            user = Student.objects.get(email=email,password=passwd)  #fetch data from student db
            request.session['user-id'] = user.stud_id
            request.session['user-email'] = user.email

            messages.success(request, f'Login successful. Welcome {user.fname}')

            if user.branch == 0 or user.year == 0 or user.div_field == None:    #if extra sign up is not done then redirect to extra sign up page
                messages.success(request, f'Please fill following details..')
                request.session['extra'] = 1            #for extra signup
                return redirect('student-extra-register')
            else:
                return redirect('student-home')     #otherwise redirect to home page
        except :
            messages.warning(request, f'Email or Password is Wrong!!')
            return redirect('student-login')
            

    return render(request, 'student/login.html')        #not request for login. directly display login page



def register(request):
    
    if Auth.auth(request):  #if user is already logged in then redirect to home page
        global messages
        #username = request.session['user-id']
        messages.warning(request, f'Logout to register')
        return redirect('student-home')

    if request.method == "POST":
        data = request.POST.copy()
        email = data.get('email')
        fname = data.get('fname')
        lname = data.get('lname')
        mono = data.get('mono')
        gender = data.get('gender')
        passwd = data.get('password')
        cpasswd = data.get('cpassword')
     
        newStudent = studentRegistration(email,fname,lname,mono,gender,passwd,cpasswd)  #create object of class studentRegis...
        message = newStudent.auth(request)      #validate data

        if message == True:
            #if true account created
            messages.success(request,f'Successfully Created Account! Login Now')
            return redirect('student-login')
        else:
            #otherwise display error messages
            messages = message
            return redirect('student-register')

    return render(request,'student/signup.html' ) #if condition is false t



#extra signup page
def register_extra(request):
    
    if request.method == "POST":
        data = request.POST.copy()
        year = data.get('year')
        div = data.get('div')
        roll_no = data.get('roll_no')
        prn_no = data.get('prn_no')
        birthday = data.get('birthday')

        message = studentRegistration.auth_extra(request,year,div,roll_no,prn_no,birthday)
        if message == True:
            return redirect('student-home')
        else:
            messages = message
            return redirect('student-extra-register')

    elif request.session.has_key('extra'):  #check session variable extra (line no 112)
        return render(request, 'student/signup-extra.html')
    else:
        messages.warning(request, f'Login First')
        return redirect('student-login')


#home page
def home(request):
    if Auth.auth(request):
        return render(request, 'student/home.html')
      
    else:
        messages.warning(request, f'Login First')
        return redirect('student-login')


#logout
def logout(request):
    
    try:
        del request.session['user-id']
        del request.session['user-email']
        del request.session['extra']
    except:
        pass
    messages.success(request, f'Logout successful')
    return redirect('student-login')
      