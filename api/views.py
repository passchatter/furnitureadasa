from django.shortcuts import render, redirect
from .forms import SignupForm

def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'api/signup.html', {
        'form':form
    })