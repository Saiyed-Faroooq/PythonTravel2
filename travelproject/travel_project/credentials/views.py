from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username/Password Invalid')
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        em = request.POST['email']
        pw = request.POST['password']
        cpw = request.POST['password1']
        if pw == cpw:
            if User.objects.filter(username=un).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            if User.objects.filter(email=em).exists():
                messages.info(request, "Email Address Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=un, password=pw, first_name=fn, last_name=ln, email=em)

            user.save()
            messages.info(request, "User Created")
            return redirect('login')
        else:
            messages.info(request, "Password Mismatch")
            return redirect('register')
    return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
