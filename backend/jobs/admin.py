from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'employment_type', 'is_active', 'created_at')
    list_filter = ('is_active', 'employment_type')
    search_fields = ('title', 'location')
