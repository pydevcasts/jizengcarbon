from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            auth_login(request, user)
            return redirect('product:product_and_category')
    else:
        form = SignUpForm()
    return render(request, 'frontend/accounts/register.html', {'form': form, 'title':"signup", "segment":"signup"})






