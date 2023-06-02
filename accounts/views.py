from django.shortcuts import redirect, render
from accounts.forms import UserForm



def SignUp(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()

    return render(request, 'registration/signup.html', {'form': form})
