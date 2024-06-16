from rest_framework.permissions import  BasePermission


class IsAdminUser(BasePermission):
    """
    Allows access to Admin users only
    """
    def has_permission(self, request, view):
        return  request.user and request.user.is_authenticated and request.user.role == "admin"


class IsCustomerUser(BasePermission):
    """
    Allows access only to customer users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'customer'
