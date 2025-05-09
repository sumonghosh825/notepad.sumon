from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Task
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registered successfully.")
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Or another page
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'authunticate/login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def task(request):
    return render(request, 'task/list.html')

def board(request):
    return render(request, 'task/board.html')

def details(request):
    return render(request, 'task/details.html')

def timeline(request):
    return render(request, 'timeline/timeline.html')

def profile(request):
    return render(request, 'profile/profile.html')

def auth_registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registered successfully. Please log in.")
        return redirect('login')

    return render(request, 'authunticate/register.html')

def auth_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')  # or any page you want to redirect after login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'profile/profile.html') 

@login_required
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        priority = request.POST.get('priority')
        time_period = request.POST.get('time_period')
        
        assigned_to_username = request.POST.get('assigned_to')
        due_date = request.POST.get('due_date')

        assigned_user = User.objects.filter(username=assigned_to_username).first()

        Task.objects.create(
            title=title,
            category=category,
            priority=priority,
            time_period=time_period,
            assigned_to=assigned_user,
            due_date=due_date,
            created_by=request.user
        )
        return redirect('task_list')

    task = Task.objects.filter(created_by=request.user).order_by('-created_at')
    users = User.objects.all()
    return render(request, 'task/list.html', {'task': task, 'users': users})


def task_list_view(request):
    task = Task.objects.all()  # You can filter by user if needed
    return render(request, 'list.html', {'task': task})
