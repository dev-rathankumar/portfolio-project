from django.shortcuts import render

# Get access to the model to pass the variable to views or home
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})