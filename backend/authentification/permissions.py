from rest_framework import permissions

class IsProPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_pro()


class IsMemberPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_member()