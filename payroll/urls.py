from django.urls import path
from . import views # . ia the current directory

urlpatterns = [
    path('', views.home, name='payroll-home'),
    path('about/', views.about, name='payroll-about'),
    path('profile/', views.profile, name='profile'), #profile
    path('attendance/', views.attendance_leave, name='attendance'),
    path('salary/', views.salary, name='salary'),
]
