from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm


def index(request):
    return render (request,"index.html")

# signup page view
# def user_signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your account has been created successfully, you can now able to login!')
#             return redirect('login')
#     else:
#         form = SignupForm(initial={'username': '', 'email': ''})   
#         return render(request, 'signup.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created successfully, you can now log in!')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# login page view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page view
def user_logout(request):
    logout(request)
    return redirect('login')



# def home(request):
    