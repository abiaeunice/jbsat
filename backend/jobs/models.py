from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Job(models.Model):
    employer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    employment_type = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
