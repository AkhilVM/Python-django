from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('shop:AllProdCat')
        else:
            messages.info(request,'invalid credentials')
            return redirect('account:login')

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        email = request.POST['Email']
        username = request.POST['Username']
        password = request.POST['Password']
        cpassword = request.POST['Confirm_password']
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken ')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                user.save();
                print('User created')
                return redirect('account:login')
        else:
            messages.info(request,'password not matching')
            return redirect('account:register')

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('shop:AllProdCat')
