from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import *

# Create your views here.
def sayhello(request):
    return HttpResponse("<br><b>Hello Django(number=40)....</b>")


def search_name(request, name = None):
    print(f"name = {name}")
    try:
        user = user.object.get(username = name)
        print(user.username)
        print(user.useremail)
        print(user.data_joined)
        return HttpResponse(f"account exit-email:{user.email}-login time:{user.data_joined}")
    except:
        return HttpResponse("not exist!!!")




def useradd(request, name=None):
    print(f"name = {name}")
    try:
        user = User.objects.get(username=name)
        return HttpResponse(f"{user.username}account build!!!<a href='/login'/>logined</a>")
    except:
        user = User.objects.create_user(name,"test@yahoo,com,tw", "1234")
        user.first_name = "Huang"
        user.last_anme = "J.R"
        user.is_staff = True
        user.is_active = True
        user.save()
        return HttpResponse(f"{user.username}accounr build over!!!<a href = '/login/'>login</a>")
    

def index(request):
    message = ""
    if request.method == "GET":
        status_message = {
            "0":"login success!!!",
            "1":"account not active!!!",
            "2":"login fail!!!"
        }
        if"status" in request.GET:
            status = request.GET["status"]
            message = status_message.get(status, "")
        print(f"message={message}")
    return render(request, "index.html", locals())
    


from django.contrib import auth
from django.shortcuts import redirect
def login(request):
    if request.method == "POST":
        name = request.POST["username"]
        password = request.POST["password"]
        print(f"name = {name}, password = {password}")
        user = auth.authenticate(username = name, password = password)
        print(f"user = {user}")      
        # if user:
        #     print(f"isaction = {user.is_actve}")
        if user:
            if user.is_active:
                auth.login(request, user)
                return redirect('/index/?status=0')
            else:
                return redirect('/index/?status=1')
        else:
            return redirect('/index/?status=2')
        # return HttpResponse("sent!")
    else:
        if request.user.is_authenticated and request.user.is_active:
            return redirect("/index/")
        else:
            return render(request, "login.html", locals())
    
def logout(request):
    auth.logout(request)
    return redirect("/index/")