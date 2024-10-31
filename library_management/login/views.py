from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login, authenticate # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
# Create your views here.'

#create a superuser admin
#logins only admin
def login_user(request):
    if request.method == 'POST':
        username = request.POST["Username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,'Incorrect Password/Username\nTry Again...')
            return redirect('login')
    else:      
        return render(request,'login.html',{})
