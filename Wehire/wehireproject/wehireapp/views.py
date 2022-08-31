from django.shortcuts import render,redirect
from django.http import HttpResponse
from .import forms, models
from django.core.mail import send_mail
from wehireproject.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import *
import uuid
from django.conf import settings
from django.contrib.auth import authenticate

def new(request):
    return render(request,'new.html')


def index(request):
    return render(request,'home.html')


# def login(request):
#     return render(request,'login1.html')


# def register(request):
#     return render(request,'register.html')


# def postJob(request):
#     return render(request,'post-job.html')


def regis(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        # phone=request.POST.get('number')
        if User.objects.filter(username=username).first():
            messages.success(request,'username already exist')
            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request,'email already registered')
            return redirect(regis)
        # if User.objects.filter(number=phone).first():
        #     messages.success(request,'Phone number already registered')
        #     return redirect(regis)

        user_obj=User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        auth_token=str(uuid.uuid4())

        profile_obj=companydetails.objects.create(user=user_obj, auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)
        return redirect('http://127.0.0.1:8000/token/')

    return render(request,'register.html')

def send_mail_regis(email,token):
    subject = 'your account has been verified'
    message = f'paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)

def verify(request,auth_token):
    profile_obj=companydetails.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'Your account is already verified')
            return redirect('http://127.0.0.1:8000/login/')
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'Your account has been verified')
        return redirect('http://127.0.0.1:8000/login/')
    else:
        return redirect('/error')

def token(request):
    return render(request,'token_send.html')

def error(request):
    return render(request,'errorpage.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'user not found')
            return redirect('http://127.0.0.1:8000/login/')
        profile_obj =companydetails.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check your mail')
            return redirect('http://127.0.0.1:8000/login/')
        user = authenticate(username=username,password=password)
        if user is None:
            messages.success(request,'wrong password or username')
            return redirect('http://127.0.0.1:8000/login/')
        # home(request,user)
        a = companydetails.objects.filter(user=user)
        return render(request, 'company-login.html',{'company':a})
    return render(request,'login1.html')


def compProfile(request):
#     company=companydetails.objects.all()
#     for i in company:
#         cmp=i.user
#         id1=i.id
    return render(request, 'company-login.html')




def registeredcompanies(request):
    regcom = User.objects.all()
    li = []
    em = []
    for i in regcom:
        username = i.username
        li.append(username)
        email = i.email
        em.append(email)
    print(li)
    print(em)
    li1 = li[1:]
    em1 = em[1:]
    print(li1)
    print(em1)
    mylist = zip(li1, em1)
    return render(request, 'registeredcompanies.html',{ 'mylist': mylist })



def editprofile(request,username,token):
    if request.method == 'POST':
        c = User.objects.filter(username=username).first()

        c.username = request.POST.get('username')
        c.email = request.POST.get('email')
        c.save()
        a=companydetails.objects.filter(auth_token=token)
        return render(request,'company-login.html',{'company':a})
    b=companydetails.objects.filter(auth_token=token).first()
    return render(request, 'editprofile.html',{'x':b})



def post_job(request):
    if request.method=='POST':
        a=postjobform(request.POST)
        if a.is_valid():
            Jobtitle1 =a.cleaned_data['Jobtitle']
            companyname1 = a.cleaned_data['companyname']
            jobdescription1 = a.cleaned_data['jobdescription']
            Experience1 = a.cleaned_data['Experience']
            workplace1 = a.cleaned_data['workplace']
            Employmenttype1 = a.cleaned_data['Employmenttype']
            b = postjob(Jobtitle=Jobtitle1, companyname=companyname1, jobdescription=jobdescription1,
                        Experience=Experience1, workplace=workplace1, Employmenttype=Employmenttype1)
            b.save()
            return HttpResponse("job posted")
        else:
            return HttpResponse("error")

    return render(request,'post-job.html')


def postdisplay(request):
    jobdisplay = postjob.objects.all()
    li = []
    em = []
    id=[]
    for i in jobdisplay:
        Jobtitle= i.Jobtitle
        li.append(Jobtitle)
        companyname = i.companyname
        em.append(companyname)
        path=i.id
        id.append(path)
    print(li)
    print(em)
    li1 = li[1:]
    em1 = em[1:]
    print(li1)
    print(em1)
    mylist = zip(li1, em1,id)
    return render(request, 'post-display.html',{ 'mylist': mylist })



def userregister(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('useremail')
        userpassword = request.POST.get('userpassword')
        userconfirm = request.POST.get('userconfirm')
        if employeemodel.objects.filter(firstname=firstname):
            messages.success(request, 'first name already exist')
            return redirect(userregister)
        if employeemodel.objects.filter(lastname=lastname):
            messages.success(request, 'last name already exist')
            return redirect(userregister)
        if employeemodel.objects.filter(username=username):
            messages.success(request, 'Username already exist')
            return redirect(userregister)
        if employeemodel.objects.filter(email=email):
            messages.success(request, 'Email already exist')
            return redirect(userregister)
        if userpassword != userconfirm:
            messages.success(request,'Password dont  match' )
            return redirect(userregister)
        if userpassword == userconfirm:
            b = employeemodel(firstname=firstname, lastname=lastname, username=username, email=email,
                              userpassword=userpassword)
            b.save()
        # a = employeemodel.objects.filter(username=username)
        return redirect(userlogin)
        # return render(request, 'post-display.html', {'user': a})
    return render(request, 'userregister.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpassword')
        b = employeemodel.objects.filter(username=username).first()
        if b is None:
            messages.success(request, 'username not found')
            return redirect(userlogin)
        c = employeemodel.objects.filter(userpassword=password).first()
        if c is None:
            messages.success(request, 'password incorrect')
            return redirect(userlogin)
        return redirect(postdisplay)
        # a = employeemodel.objects.filter(username=username)
        # return render(request, 'user_profile.html', {'user': a})
    return render(request, 'userlogin.html')




def readmore(request, id):
        a = postjob.objects.filter(id=id+1)
        return render(request, 'Job-readmore.html', {'x': a})


def apply(request,title,company_name):
    if request.method=='POST':
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        country_code=request.POST.get('country_code')
        phone=request.POST.get('phone')

        resume=request.FILES['resume']

        current_position=request.POST.get('current_position')
        current_company=request.POST.get('current_company')

        title=title
        cmp_name=company_name

        a=apply_job.objects.create(full_name=full_name,email=email,phone=phone,resume=resume,current_position=current_position,current_company=current_company,job_title=title,company_name=cmp_name)
        a.save()
        messages.success(request,'applied succesfully')
        return redirect(postdisplay)


    return render(request,'apply.html')



def companyjobs(request,cname):
    a = postjob.objects.filter(companyname=cname)
    return render(request,'jobsapplied.html',{'job':a})


def viewapplicants(request,companyname,title):
    a = apply_job.objects.filter(company_name=companyname, job_title=title)
    li = []
    for i in a:
        path = i.resume
        li.append(str(path).split('/')[-1])
    context = zip(a, li)
    return render(request, 'applicants_view.html', {'x': context})




