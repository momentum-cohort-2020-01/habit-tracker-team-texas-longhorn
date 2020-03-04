from django.contrib import admin
from .models import Habit, Activity, Record

admin.site.register(Habit)
admin.site.register(Activity)
admin.site.register(Record)