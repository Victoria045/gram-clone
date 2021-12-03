from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has neen created! You are now able to log in {username}.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})  

# @login_required(login_url='login')
def index(request):
    
    return render(request, 'gram/index.html',)