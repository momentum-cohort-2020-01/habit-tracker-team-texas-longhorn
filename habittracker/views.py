from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Habit, Activity, User
from .forms import HabitForm, ActivityForm


@login_required
def homepage(request):
    return render(request, 'habittracker/index.html')
 
# def habits(request):
#     habits = Habit.objects.all()
#     return render(request, 'habittracker/index.html', {'habits': habits})

# def habits_detail(request, pk):
#     habit = Habit.objects.get(pk=pk)
#     return render(request, 'habittracker/habits_detail.html', {'habit': habits, 'pk': pk})

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


# def edit_habit(request, pk):
#     habit = get_object_or_404(Habit, pk=pk)
#     if request.method == "POST":
#         form = HabitForm(request.POST, instance=habit)
#         category = request.POST.get('category')
#         form.fields['category'].choices = [(category, category)]

#         if form.is_valid():
#             habit = form.save()
#             form.save()
#             return redirect('habits')
#     else:
#         form = HabitForm(instance=habit)
#         return render(request, 'habittracker/edit_habit.html', {'form': form})

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
