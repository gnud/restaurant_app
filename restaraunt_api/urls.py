from django.urls import include, path
from rest_framework import routers

from restaraunt_api import api

router = routers.DefaultRouter()
router.register(r'orders', api.OrderViewSet, basename='orders')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
