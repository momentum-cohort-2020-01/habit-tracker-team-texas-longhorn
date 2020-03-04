from django.shortcuts import render
from .models import Habit, Activity, Record
# Create your views here.

def homepage(request):
    return render(request, 'habittracker/index.html')