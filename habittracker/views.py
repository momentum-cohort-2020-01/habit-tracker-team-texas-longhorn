import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Habit, Activity, User, Observer
from .forms import HabitForm, ActivityForm, ObserverForm


@login_required(login_url='/accounts/login')
def homepage(request):
    return render(request, 'habittracker/index.html')


@login_required(login_url='/accounts/login')
def habits_detail(request):
    my_habits = Habit.objects.all().filter(user=request.user)
    return render(request, 'habittracker/habits_detail.html', {'my_habits': my_habits})


@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login')
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save()
            form.save()
            return redirect('habits')
    else:
        form = HabitForm(instance=habit)
        return render(request, 'habittracker/edit_habit.html', {'form': form})


@login_required(login_url='/accounts/login')
def progress(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    activities = Activity.objects.all().filter(habit=habit).order_by('created_at')
    day = 0
    results_y = []
    dates_x = []
    goal_data = []

    for activity in activities:
        day += 1
        results_y.append(activity.result_nbr)
        dates_x.append(f'DAY {day}')
        goal_data.append(habit.goal_nbr)

    return render(request, 'habittracker/progress.html', {'habit': habit, 'results_y': results_y, 'dates_x': dates_x, 'goal_data': goal_data})


def logout(request):
    return redirect('homepage')


@login_required(login_url='/accounts/login/')
def link_observer(request, pk):
    user = User.objects.get(username=request.user.username)
    habit = Habit.objects.get(pk=pk)
    if request.method == "POST":
        try:
            linked_observer = User.objects.get(
                username=request.POST['observer'])
        except ObjectDoesNotExist:
            form = ObserverForm()
            context = {'form': form,
                       'Alert': "Invalid username. Try again."}
            return render(request, 'habittracker/link_observer.html', context=context)

        if habit.owner != user:
            return redirect('/')
        elif Observer.objects.filter(observer=linked_observer, habit=habit):
            form = ObserverForm()
            context = {'form': form,
                       'Alert': "Oops! User already linked as observer"}
            return render(request, 'habittracker/link_observer.html', context=context)

        elif linked_observer == habit.owner:
            form = ObserverForm()
            context = {'form': form,
                       'Alert': 'Oh no! Cannot link yourself as observer'}
            return render(request, 'habittracker/link_observer.html', context=context)

        else:
            observer = Observer(habit=habit, observer=linked_observer)
            observer.save()
            # redirect to observer detail.html?
            return redirect('habits_detail', pk)
    else:
        form = ObserverForm()
    return render(request, 'habittracker/link_observer.html', {'form': form})


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
