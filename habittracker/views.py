from django.shortcuts import render
from .models import Habit, Record, Activity
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    return render(request, 'habittracker/index.html')