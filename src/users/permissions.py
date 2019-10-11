from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permisson to only allow profile owner to edit it
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user