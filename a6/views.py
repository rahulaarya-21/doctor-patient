#from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from random import *
from .utils import *
from django.core.mail import send_mail

# Create your views here.
#def homepage(request):
    #return render(request,"app/home.html")

def Indexpage(request):
    return render(request,"app/index.html")

def RegisterPage(request):
    try:
        if request.POST['role']=='doctor':
            role=  request.POST['role']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            password=request.POST['password']
            confirmpassword=request.POST['confirmpassword']
            gender=request.POST['gender']
            email=request.POST['email']
            speciality=request.POST['speciality']
            dateofbirth=request.POST['birthdate']
            city=request.POST['city']
            mobile=str(request.POST['phone'])
            user=User.objects.filter(email=email)
            upload_img=request.FILES['image']
            if user:
                message='This email already existed'
                return render(request,"app/index.html",{'message':message})
            else:
                if password==confirmpassword:
                    otp=randint(100000,999999)
                    newuser=User.objects.create(email=email,password=password,role=role,otp=otp)
                    newdoctor=Doctor.objects.create(user_id=newuser, firstname=firstname,profile_pic=upload_img, lastname=lastname,
                                                      gender=gender, speciality=speciality, city=city, mobile=mobile, birthdate=dateofbirth)
                    email_subject = "Doctor Finder : Account Vericication"
                    sendmail(email_subject, 'mail_templates', email, {
                             'name': firstname, 'otp': otp, 'link': 'http://localhost:8000/enterprise/user_verify/'})
                    return render(request, 'app/Success.html')
                else:
                    message = "Password and confirm password doesn't match"
                    return render(request, 'app/success.html', {'message': message})
        else:
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            confirmpassword = request.POST['confirm']
            gender = request.POST['gender']
            email = request.POST['email']
            dateofbirth = request.POST['birthdate']
            city = request.POST['city']
            mobile = str(request.POST['phone'])
            user = User.objects.filter(email=email)
            upload_img=request.FILES['image']

            if user:
                message = 'This email already exists'
                return render(request, 'app/index.html', {'message': message})
            else:
                if password == confirmpassword:
                    otp = randint(100000, 9999999)
                    newuser = User.objects.create(
                        email=email, password=password, role=role, otp=otp)
                    newpatient = Patient.objects.create(
                        user_id=newuser, firstname=firstname, lastname=lastname,profile_pic=upload_img, gender=gender, city=city, mobile=mobile, birthdate=dateofbirth)
                    email_subject = "Doctor Finder : Account Vericication"
                    sendmail(email_subject, 'mail_templates', email, {
                             'name': firstname, 'otp': otp, 'link': 'http://localhost:8000/enterprise/user_verify/'})
                    return render(request, 'app/Success.html')
                else:
                    message = "Password and confirm password doesn't match"
                    return render(request, 'app/success.html', {'message': message})
    except User.DoesNotExist:
        message = 'This email already exists'
        return render(request, 'app/index.html', {'message': message})
    
def show(request):
    return render(request,"app/success.html")