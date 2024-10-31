from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
#log out's the admin   
def logout_user(request):
    logout(request)
    return redirect('login')

def catalog(request):
    return render(request, 'catalog.html', {})

    