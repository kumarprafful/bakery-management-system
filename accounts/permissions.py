from rest_framework.permissions import BasePermission

class IsBakeryAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.user_role == 1)

class IsCustomerAuthenticated(BasePermission):
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.user_role == 2)