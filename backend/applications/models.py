from django.db import models
from django.conf import settings
from jobs.models import Job

User = settings.AUTH_USER_MODEL

class Application(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Reviewing', 'Reviewing'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'seeker')

    def __str__(self):
        return f"{self.seeker} → {self.job}"
