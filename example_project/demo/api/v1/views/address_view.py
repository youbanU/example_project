from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.compat import coreapi

from demo.api.v1.services.address_create_service import address_update_, address_create_
from demo.models import Address
from demo.api.v1.selectors.address_get_selector import address_get_


class AddressViewSet(ModelViewSet):
    """
    Address API

    """
    class AddressSerializer(serializers.ModelSerializer):
        class Meta:
            model = Address
            fields = (
                'id', 'address', 'street_number', 'city', 'state', 'zip_code',)
            extra_kwargs = {
                "id": {"read_only": True},
                "address": {"required": True,
                               "error_messages": {"required": "First name is required field.",
                                                  "blank": "First name is non blank field"}}
            }

    serializer_class = AddressSerializer
    permission_classes = (AllowAny,)
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_param_fields(self, view):
        fields = [
            coreapi.Field(
                name='address',
                required=False,
                location='query',
                description='',
                example='',
                type='',
            ),
            coreapi.Field(
                name='city',
                required=False,
                location='query',
                description='',
                example='',
                type='',
            ),
            coreapi.Field(
                name='state',
                required=False,
                location='query',
                description='',
                example='',
                type='',
            )
        ]
        return fields


    def get_queryset(self):
        return address_get_(self.request.query_params, self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request)
        if response.data:
            return Response({'data': response.data, 'message': 'success'},
                            status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = address_create_(request.data, request.user)
        if response:
            return Response(
                {
                    'data': self.serializer_class(response).data,
                    'message': 'success'
                }, status=status.HTTP_201_CREATED
            )

    def update(self, request, *args, **kwargs):

        try:
            person = Address.objects.get(id=kwargs['pk'])
            response = address_update_(person, request.data, request.user)
            if response:
                serializer = self.serializer_class(response)
                return Response({
                    'data': serializer.data,
                    'message': 'success'}, status=status.HTTP_200_OK)
        except Address.DoesNotExist:
            return Response({'message': 'Address not found'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = Address.objects.get(id=kwargs['pk'])
            instance.delete()
            return Response({'message': 'success'}, status=status.HTTP_204_NO_CONTENT)
        except Address.DoesNotExist:
            return Response({'message': 'Address not found'}, status=status.HTTP_400_BAD_REQUEST)
