import datetime

from rest_framework import permissions


class CanPlaceOrderPermission(permissions.BasePermission):
    message = 'Can the owner place an order.'

    def has_permission(self, request, view):
        from restaraunt_api.models import Order

        # We assume is action create
        if request.method == 'POST':
            dt = datetime.datetime.now()
            has_order_today = Order.objects.filter(
                date_ordered__date=dt, user=request.user
            ).exists()

            if has_order_today:
                return False

        return super().has_permission(request, view)
