from django.contrib import admin
from django.urls import path, include
from habittracker import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('new_habit/', views.new_habit, name='new_habit'),
    path('accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns