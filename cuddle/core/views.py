from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from item.models import Item    

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]

    return render(request, 'core/index.html', {
        'items': items
    })

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form 
    })