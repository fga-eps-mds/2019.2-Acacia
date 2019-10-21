from rest_framework.permissions import BasePermission
from rest_framework import permissions

class UserIsPropertyOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permition(self, request, view, property):
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return request.user.id == property.owner.id