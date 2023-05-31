from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from requests import request

from accounts.forms import UserForm


def SignUp1(request):
    #form_class = UserForm
    #success_url = reverse_lazy('login')
    #template_name = 'registration/signup.html'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
    else:
        form = UserForm()

    return render(request, 'registration/signup.html', {'form': form})



def SignUp(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()

    return render(request, 'registration/signup.html', {'form': form})