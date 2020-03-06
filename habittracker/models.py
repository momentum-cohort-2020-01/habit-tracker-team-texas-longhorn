from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Habit(models.Model):
    name = models.CharField(max_length=60)
    goal_nbr = models.IntegerField(default=0, null=True, blank=True)
    goal_description = models.CharField(max_length=60, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, related_name="habit", on_delete=models.CASCADE)

    @property
    def duration(self):
        delta = self.end_date - self.start_date
        return f'{delta} days'

    def __str__(self):
        return f"Your chosen habit is {self.name}, with a goal of {self.goal_nbr} {self.goal._description} for {self.duration} days, from {self.start_date} to {self.end_date}"


class Activity(models.Model):
    # name = models.CharField(max_length=60)
    result_nbr = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(
        User, related_name="activity", on_delete=models.CASCADE)
    habit = models.ForeignKey(
        'Habit', related_name="activity", on_delete=models.CASCADE)

    @property
    def diff_between_goal_result(self):
        diff_nbr = result_nbr - self.habit.goal_nbr
        return f'{ diff_nbr }'

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['created_at', 'habit'], name='one_update_per_day'), ]

    def __str__(self):
        return f"Today you achieved: {self.result_nbr} of your {self.habit.name} {self.habit.goal_description}"


# class Record(models.Model):
#     user = models.ForeignKey(
#         User, related_name="record", on_delete=models.CASCADE)

#     def __str__(self):
#         return f'Record: {self.habit, self.activity}'


# class Category(models.Model):
#     name = models.CharField(max_length=60)
#     habit = models.ManyToManyField(
#         Habit, related_name='category'
#     )
#     activity = models.ManyToManyField(
#         Activity, related_name='category'
#     )

#     def __str__ (self):
#         return f'{self.name}'
