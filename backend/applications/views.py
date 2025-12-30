from rest_framework import generics, permissions, status
from rest_framework.exceptions import ValidationError
from .models import Application
from .serializers import ApplicationSerializer, ApplicationStatusSerializer
from .permissions import IsSeeker, IsEmployerOwner
from jobs.models import Job
from rest_framework.views import APIView
from rest_framework.response import Response


class ApplyJobView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsSeeker]

    def perform_create(self, serializer):
        job_id = self.request.data.get('job')
        job = Job.objects.get(id=job_id)

        if Application.objects.filter(job=job, seeker=self.request.user).exists():
            raise ValidationError("You have already applied to this job.")

        serializer.save(seeker=self.request.user, job=job)

class SeekerApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsSeeker]

    def get_queryset(self):
        return Application.objects.filter(seeker=self.request.user)

class EmployerApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(job__employer=self.request.user)

class ApplicationStatusUpdateView(generics.UpdateAPIView):
    serializer_class = ApplicationStatusSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployerOwner]
    queryset = Application.objects.all()

class EmployerDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        jobs = Job.objects.filter(employer=request.user)
        data = []

        for job in jobs:
            applications = Application.objects.filter(job=job)
            data.append({
                "job_id": job.id,
                "job_title": job.title,
                "applications": ApplicationSerializer(applications, many=True).data
            })

        return Response(data)

