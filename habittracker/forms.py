from django.forms import ModelForm
from .models import Habit, Activity
from django.utils.translation import ugettext_lazy as _

class HabitForm (ModelForm):
    class Meta:
        model = Habit
        fields = ('name', 'goal_text', 'goal_nbr')
        labels = {
            'name': _('Title of this habit-tracker:'),
            'goal_text': _('Activity to improve:'),
            'goal_nbr': _('Numeric goal:'),
        }

class ActivityForm (ModelForm):
    class Meta:
        model = Activity
        fields = ('category', 'result', 'habit')
        labels = {
            'category': _('Activity:'),
            'habit': _('Select habit you worked on:'),
            'result': _('Numeric result for today:'),
        }
        # will need to pass Habit.goal_text as context