from rest_framework.permissions import BasePermission

class IsSeeker(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'SEEKER'

class IsEmployerOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.job.employer == request.user
