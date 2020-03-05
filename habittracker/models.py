from django.db import models
from django.contrib.auth.models import User


class Habit(models.Model):
    name = models.CharField(max_length=60)
    goal_nbr = models.IntegerField(default=0, null=True, blank=True)
    goal_text = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, related_name="habit", on_delete=models.CASCADE)

    def __str__ (self):
        return f'Goal: {self.goal_text} Target Number: {self.goal_nbr}'


class Activity(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    result = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(
        User, related_name="activity", on_delete=models.CASCADE)
    habit = models.ForeignKey(
        'Habit', related_name="activity", on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['created_at', 'habit'], name='one_update_per_day'),]
    
    def __str__ (self):
        return f'{self.name}'


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