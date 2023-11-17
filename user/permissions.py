from rest_framework import permissions

class IsCreationOrIsAthenticated(permissions.BasePermission):
    # def has_object_permission(self, request, view):
    #     return bool(request.user and request.user.is_authenticated)
        
