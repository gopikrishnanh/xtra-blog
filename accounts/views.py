from profile import Profile

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from bloghome.models import Post


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
        return render(request, 'registeration.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if password == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email.taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                print('User created')
        else:
            print("Password not matched")
            return redirect('register')
        return redirect("/")
    else:
        return render(request, 'registeration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


