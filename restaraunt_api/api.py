from rest_framework import viewsets
from rest_framework import permissions

from restaraunt_api.models import Order
from restaraunt_api.permissions import CanPlaceOrderPermission
from restaraunt_api.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that manages orders for the customers to use
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        CanPlaceOrderPermission,
    ]

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                user=self.request.user
            )
        )
