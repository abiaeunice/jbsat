from rest_framework import generics, permissions
from .models import Job
from django.db.models import Q
from .serializers import JobSerializer
from .permissions import IsEmployer

class PublicJobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Job.objects.filter(is_active=True)

        title = self.request.query_params.get('title')
        location = self.request.query_params.get('location')
        employment_type = self.request.query_params.get('employment_type')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if location:
            queryset = queryset.filter(location__icontains=location)

        if employment_type:
            queryset = queryset.filter(employment_type__iexact=employment_type)

        return queryset

class EmployerJobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsEmployer]

    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)

class EmployerJobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsEmployer]

    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user)
