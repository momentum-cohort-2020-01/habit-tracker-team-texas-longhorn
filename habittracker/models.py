from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    record = models.ForeignKey(
        "Record", related_name="user", on_delete=models.CASCADE)


class Habit(models.Model):
    name = models.CharField(max_length=60)
    goal_nbr = models.IntegerField(default=0)
    goal_text = models.CharField(max_length=60)
    user = models.ForeignKey(
        "User", related_name="habit", on_delete=models.CASCADE)
    record = models.ForeignKey(
        "Record", related_name="habit", on_delete=models.CASCADE)


class Activity(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateField(auto_now=True)
    result = models.IntegerField(default=0)
    user = models.ForeignKey(
        "User", related_name="activity", on_delete=models.CASCADE)
    habit = models.ManyToManyField(
        "Habit", related_name="activity", on_delete=models.CASCADE)


class Record(models.Model):
    def __str__(self):
        return f'Record: {self.habit, self.activity}'
