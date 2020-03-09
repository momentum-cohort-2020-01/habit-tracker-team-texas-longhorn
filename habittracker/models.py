from django.db import models
from django.contrib.auth.models import User
import datetime

GOAL_EVALUATE = (
    ('Daily Average', 'DAILY AVERAGE'),
    ('Weekly Average', 'WEEKLY AVERAGE'),
    ('Daily Total', 'DAILY TOTAL'),
    ('Weekly Total', 'WEEKLY TOTAL'),
    ('Total', 'TOTAL'),
)


class Habit(models.Model):
    name = models.CharField(max_length=60)
    goal_nbr = models.IntegerField(default=0, null=True, blank=True)
    goal_description = models.CharField(max_length=60, null=True, blank=True)
    eval_method = models.CharField(max_length=100, choices=GOAL_EVALUATE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, related_name="habit", on_delete=models.CASCADE)

    @property
    def duration(self):
        delta = self.end_date - self.start_date
        return f'{delta.days} days'

    # I'll explain my reasoning today about why I think this is too much in the string method.
    # def __str__(self):
    #    return f"My Goal: {self.name} {self.goal_nbr} {self.goal_description} for {self.duration} from {self.start_date} to {self.end_date}"

    @property
    def days_remaining(self):
        today = datetime.date.today()
        remaining = self.end_date - today
        return remaining.days

    # @property
    # def status(self):

    def __str__(self):
        return f"{self.name}"


class Activity(models.Model):
    # name = models.CharField(max_length=60)
    result_nbr = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateField(default=datetime.date.today)
    updated_at = models.DateField(auto_now=True)
    # user = models.ForeignKey(
    #     User, related_name="activity", on_delete=models.CASCADE)
    habit = models.ForeignKey(
        'Habit', related_name="activity", on_delete=models.CASCADE)

    @property
    def diff_between_goal_result(self):
        diff_nbr = self.result_nbr - self.habit.goal_nbr
        return diff_nbr

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['created_at', 'habit'], name='one_update_per_day'), ]

    def __str__(self):
        return f'{self.result_nbr} on {self.created_at}'


class Observer(models.Model):
    observer = models.ForeignKey(
        User, related_name='observations', on_delete=models.CASCADE)
    habit = models.ForeignKey(
        Habit, related_name='observers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns observer primary key linked to user habit
        return f"User: {self.observer.pk} => Habit: {self.habit.pk}"

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['observer', 'habit'], name='unique_observers'),
        ]


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
