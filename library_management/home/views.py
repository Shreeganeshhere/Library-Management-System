from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
#log out's the admin   
def logout_user(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'index2.html', {})

    