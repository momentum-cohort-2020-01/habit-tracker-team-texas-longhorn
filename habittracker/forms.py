from django.forms import ModelForm
from .models import Habit, Activity

class HabitForm (ModelForm):
    class Meta:
        model = Habit
        fields = ('name', 'goal_text', 'goal_nbr')

class ActivityForm (ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'category', 'result')
        # will need to pass Habit.goal_text as context