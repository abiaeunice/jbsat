from django.urls import path
from .views import (
    ApplyJobView,
    SeekerApplicationListView,
    EmployerApplicationListView,
    EmployerDashboardView,
    ApplicationStatusUpdateView,
)


urlpatterns = [
    path('apply/', ApplyJobView.as_view()),
    path('seeker/', SeekerApplicationListView.as_view()),
    path('employer/', EmployerApplicationListView.as_view()),
    path('employer/dashboard/', EmployerDashboardView.as_view()),
    path('<int:pk>/status/', ApplicationStatusUpdateView.as_view()),
    
]
