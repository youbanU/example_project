from django.urls import path, re_path
from rest_framework import routers

from demo.api.v1.views.person_view import PersonViewSet

from demo.api.v1.views.address_view import AddressViewSet

router = routers.DefaultRouter()

router.register(r'person', PersonViewSet, basename='person-apis')
router.register(r'address', AddressViewSet, basename='address-apis')

urlpatterns = []

urlpatterns += router.urls
