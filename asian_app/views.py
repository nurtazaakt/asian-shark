from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect # type: ignore 
from .models import Category, Job, Likes, Information
from django.contrib.auth import login, authenticate, logout # type: ignore
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm     # type: ignore


def home_page(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()

    context = {
        'categories': categories,
        'jobs': jobs
    }
    return render(request, 'home.html', context)

def jobs_page(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs
    }
    return render(request, "jobs.html", context)

def categories_page(request):
    categories = Category.objects.all() 
    context = {
        'categories': categories
    }
    return render(request, "categories.html", context)

def likes_page(request):
    likes_list = Likes.objects.all() 
    context = {
        'likes': likes_list
    }
    return render(request, "liked.html", context)

def information_page(request):
    infos = Information.objects.all() 
    context = {
        'infos': infos
    }
    return render(request, "information.html", context)

def job_infromations_page(request, pk):
    job = get_object_or_404(Job, pk=pk)
    context = {
        'job': job
    }
    return render(request, "job-informations.html", context)

def guide_job_page(request, pk):
    guide = get_object_or_404(Information, pk=pk)
    context = {
        'guides': guide
    }
    return render(request, "guide_job.html", context)

def Joe_Biden_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    jobs = Job.objects.filter(category=category)
    context = {
        'category': category,
        'jobs': jobs
    }
    return render(request, "joe Baiden.html", context)

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }   
    return render(request, "registration_page.html", context)

def log_in_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, "login_page.html", context)

def logout_action(request):
    logout(request)
    return redirect('home_page')