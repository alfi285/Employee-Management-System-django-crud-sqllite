from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Signup view
def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def loginpage(request):
    if request.method == 'POST':
        usr = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=usr, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials. Try again'})
    return render(request, 'login.html')


# Home view
def home(request):
    if request.user.is_authenticated:
        return render(request, 'Home.html')
    else:
        return redirect('login')

# Logout view
def logoutpage(request):
    logout(request)
    return redirect('login')

# Add employee
def addemployee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewemployee')
    else:
        form = AddEmployeeForm()
    return render(request, 'addemployee.html', {'form': form})

# View employees
def viewemployee(request):
    employees = Employee.objects.all()
    return render(request, 'viewemployee.html', {'employees': employees})

# Delete employee
def deleteemployee(request, empid):
    data = Employee.objects.get(empid=empid)
    data.delete()
    return redirect('viewemployee')

# Edit employee
def editemployee(request, empid):
    data = Employee.objects.get(empid=empid)
    form = AddEmployeeForm(instance=data)
    return render(request, 'editemployee.html', {'data': data, 'form': form})

# Update employee
def updateemployee(request, empid):
    data = Employee.objects.get(empid=empid)
    form = AddEmployeeForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        form.save()
        return redirect('viewemployee')
    return render(request, 'editemployee.html', {'data': data, 'form': form})
