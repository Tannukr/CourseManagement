from django.urls import path
from .views import (
    LoginView, RegisterView, StudentDashboardView, 
    FacultyDashboardView, IndexView, LogoutView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('student-dashboard/', StudentDashboardView.as_view(), name='student-dashboard'),
    path('faculty-dashboard/', FacultyDashboardView.as_view(), name='faculty-dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
