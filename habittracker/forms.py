from django.forms import ModelForm
from .models import Habit, Activity, Observer
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django import forms


class HabitForm (ModelForm):
    class Meta:
        model = Habit
        fields = ('name', 'goal_nbr', 'goal_description', 'eval_method',
                  'start_date', 'end_date')
        labels = {
            'name': _('Habit:'),
            'goal_nbr': _('Goal Number:'),
            'goal_description': _('Unit of Measure:'),
            'eval_method': _('Evaluate:'),
            'start_date': _('Start Date:'),
            'end_date': _('End Date:'),
        }
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date'}),
        }


class ActivityForm (ModelForm):
    class Meta:
        model = Activity
        fields = ('created_at', 'habit', 'result_nbr')
        labels = {
            'created_at': _('Date of Completion:'),
            'habit': _('Habit:'),
            'result_nbr': _('Enter your result:'),
        }
        widgets = {
            'created_at': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date'}),
        }


class ObserverForm(forms.ModelForm):

    class Meta:
        model = Observer
        fields = ('observer',)
        widgets = {
            'observer': forms.TextInput()
        }
        help_texts = {
            'Observer': "Select username to link as an observer to your habit (case-sensitive)",
        }
