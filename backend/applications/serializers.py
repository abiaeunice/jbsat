from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    seeker_email = serializers.ReadOnlyField(source='seeker.email')
    job_title = serializers.ReadOnlyField(source='job.title')
    job_location = serializers.ReadOnlyField(source='job.location')
    employment_type = serializers.ReadOnlyField(source='job.employment_type')

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('status', 'seeker', 'applied_at')

class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('status',)

    def validate_status(self, value):
        valid_statuses = ['New', 'Reviewing', 'Rejected', 'Accepted']
        if value not in valid_statuses:
            raise serializers.ValidationError("Invalid application status.")
        return value