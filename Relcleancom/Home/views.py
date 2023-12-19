from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Contact

# Create your views here.


def index(request):
    context = {
        'variable':"this is done succsssfully"
    }
   # return HttpResponse("this is Homepage")
    return render(request,'index.html',context)
# def home(request):
#     return render(request,'home1.html')

def about(request):
    return render(request,'about.html')
def apart(request):
    return render(request,'apart.html')
def window(request):
    return render(request,'window.html')
def commer(request):
    return render(request,'commer.html')
def resid(request):
    return render(request,'resid.html')
def renov(request):
    return render(request,'renov.html')

def services(request):

    return render(request,'services.html')

def pricing(request):
    return render(request,'pricing.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone'),
        message = request.POST.get('message'),
        contact_data = Contact(name=name, email=email, phone=phone, message=message)
        contact_data.save()
    return render(request, 'Contact.html')


def Register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        city = request.POST['city']
        country = request.POST['country']
        gender = request.POST['gender']
        if User.objects.filter(username = username).exists():
            messages.error(request,"Username already exists")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            user = User.objects.create(username=username,first_name=fname,last_name=lname, email=email,password=password)
            user.save()
            if user is not None:
                auth.login(request, user)
                return render(request, 'home1.html')

    else:
        return render(request,'Login.html')

def register_del(request,pk):
    return redirect('Register')


def logout(request):
    auth.logout(request)
    return redirect('Login')

def home1(request):
    return render(request,'home1.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home1')
        else:
            messages.error(request,"Wrong Credentials")
            return render(request, 'Login.html')

    else:

        return render(request, 'Login.html')

def clean_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cont=Contact.objects.filter(name__contains= searched)
        return render(request, 'clean_search.html',{'searched':searched,'cont':cont})
    else:
        return render(request,'clean_search.html')



