from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Department, Course,Material
from django.http import JsonResponse, HttpResponse


# Create your views here.
def demo(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'login.html')
def dept(request):
    c_user=request.user
    #return HttpResponse( c_user.username)
    return render(request, 'form_dep.html',{'name':c_user})

def register(request):
    if request.method=='POST':
        user=request.POST['name']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        if pwd==cpwd:
            if User.objects.filter(username=user).exists():
                messages.info(request,"Username already exist")
                return redirect('collegeapp:register')
            else:
                user=User.objects.create_user(username=user,password=pwd)
                user.save();
                return redirect('collegeapp:login')

        else:
            messages.info(request, "password incorrect")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        usern=request.POST['name']
        pwd=request.POST['pwd']
        user=auth.authenticate(username=usern,password=pwd)
        if user is not None:
            auth.login(request,user)
            #return redirect('/')
            return render(request, 'new.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect('collegeapp:login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return render(request,'home.html')

def get_topics_ajax(request):
    if request.method == "POST":
        subject_id = request.POST['subject_id']
        try:
            subject = Department.objects.filter(name = subject_id).first()
            topics = Course.objects.filter(dept = subject)
        except Exception:
            data = 'error'
            return JsonResponse(data)
        return JsonResponse(list(topics.values('id', 'name')), safe = False)


def formdept(request):
    if request.method=='POST':
        user=request.user
        cid=user.id
        dob = request.POST['dob']
        age = request.POST['age']
        gen = request.POST['gen']
        ph = request.POST['ph']
        email = request.POST['email']
        add = request.POST['add']
        dept = request.POST['dept']
        cou = request.POST['cou']
        pou = request.POST['pur']
        mat1 = request.POST.getlist('mat')


        cr=Material.objects.create(uid=cid,dob=dob,age=age,gen=gen,ph=ph,mail=email,add=add,dept=dept,cou=cou,pur=pou,mat=mat1)
        cr.save();
        messages.info(request, 'Order Confirmed')



    return render(request,'form_dep.html')