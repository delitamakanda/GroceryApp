from collections import namedtuple
from rest_framework import permissions
from django.core.validators import RegexValidator

ORDER_STATUSES = namedtuple('ORDER_STATUSES', ['PENDING', 'ACCEPTED', 'REJECTED', 'CANCELLED'])._make(range(4))

ORDER_STATUSES = (
    (ORDER_STATUSES.PENDING, 'PENDING'),
    (ORDER_STATUSES.ACCEPTED, 'ACCEPTED'),
    (ORDER_STATUSES.REJECTED, 'REJECTED'),
    (ORDER_STATUSES.CANCELLED, 'CANCELLED'),
)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `user`.
        return obj.user == request.user


phone_message = 'Phone number must be entered in the format: 05999999999'

# your desired format
phone_regex = RegexValidator(regex=r'^(\d{2})\d{8}$', message=phone_message)
