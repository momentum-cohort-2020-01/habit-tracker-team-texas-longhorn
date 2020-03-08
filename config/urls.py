from django.contrib import admin
from django.urls import path, include
from habittracker import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('detail/', views.habits_detail, name='habits_detail'),
    path('new_habit/', views.new_habit, name='new_habit'),
    path('edit_habit/<int:pk>', views.edit_habit, name='edit_habit'),
    path('progress/<int:pk>', views.progress, name='progress'),
    path('new_activity/', views.new_activity, name='new_activity'),
    path('accounts/logout', views.logout, name='logout'),
    path('accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns