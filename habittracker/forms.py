from django.forms import ModelForm
from .models import Habit, Activity
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class HabitForm (ModelForm):
    class Meta:
        model = Habit
        fields = ('name', 'goal_nbr', 'goal_description',
                  'start_date', 'end_date')
        labels = {
            'name': _('Habit:'),
            'goal_nbr': _('Goal Nbr:'),
            'goal_description': _('Goal Description:'),
            'start_date': _('Habit start date:'),
            'end_date': _('Habit end date:'),
        }


class ActivityForm (ModelForm):
    class Meta:
        model = Activity
        fields = ('habit', 'result_nbr')
        labels = {
            'habit': _('Habit:'),
            'result_nbr': _('Enter your actual result'),
        }
