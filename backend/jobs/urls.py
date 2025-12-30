from django.urls import path
from .views import (
    PublicJobListView,
    EmployerJobListCreateView,
    EmployerJobDetailView,
)

urlpatterns = [
    path('public/', PublicJobListView.as_view()),
    path('employer/', EmployerJobListCreateView.as_view()),
    path('employer/<int:pk>/', EmployerJobDetailView.as_view()),
]
