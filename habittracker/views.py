import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Habit, Activity, User
from .forms import HabitForm, ActivityForm


@login_required
def homepage(request):
    return render(request, 'habittracker/index.html')

def habits_detail(request):
    my_habits = Habit.objects.all().filter(user = request.user)
    return render(request, 'habittracker/habits_detail.html', {'my_habits': my_habits})
    
def new_habit(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('homepage')
    else:
        form = HabitForm()
    return render(request, 'habittracker/new_habit.html', {'form': form})


def new_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('homepage')
    else:
        form = ActivityForm()
    return render(request, 'habittracker/new_activity.html', {'form': form})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        category = request.POST.get('category')
        form.fields['category'].choices = [(category, category)]

        if form.is_valid():
            habit = form.save()
            form.save()
            return redirect('habits')
    else:
        form = HabitForm(instance=habit)
        return render(request, 'habittracker/edit_habit.html', {'form': form})


def progress(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    activities = Activity.objects.all().filter(habit = habit).order_by('created_at')
    results_y = [activity.result_nbr for activity in activities]
    dates_x = [activity.created_at for activity in activities]
    return render(request, 'habittracker/progress.html', {'habit': habit, 'results_y': results_y, 'dates_x': dates_x})


# def habits_by_category(request, slug):
#     category = Category.objects.get(slug=slug)
#     habits_for_category = Habit.objects.filter(category=category)
#     return render(request, 'habittracker/habits_by_category.html', {'habits': habits_by_category, 'category': category})

# def get_habit_activity_for_user(request):
#     user = User.objects.get(username=request.user.username)
#     activity_habits = Habit.objects.filter(activity=True)
#     return render(request, 'habittracker/habits__by_activities.html', {'habits': activity_habits, 'user': user})

# def get_record_for_user(request):
#     user = User.objects.get(username=request.user.username)
#     records_habits = Habit.objects.filter(record=True)
#     return render(request, 'habittracker/records__by_habits.html', {'habits': records_habits, 'user': user})
