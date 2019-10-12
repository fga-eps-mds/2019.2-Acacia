from rest_framework.permissions import BasePermission

class UserIsPropertyOwner(BaseException):
    def has_object_permition(self, request, view, property):
        return request.user.id == property.owner.id