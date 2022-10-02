from rest_framework import serializers, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.compat import coreapi

from demo.api.v1.services.person_create_service import person_create_
from demo.models import Person
from demo.api.v1.selectors.person_get_selector import person_get_
from demo.utils import QueryParamSchemaFilter

from demo.models import Address

from demo.api.v1.services.person_create_service import person_update_


class PersonAddressSerializer(serializers.ModelSerializer):
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


class PersonViewSet(ModelViewSet):
    """
    Person API

    """

    class PersonSerializer(serializers.ModelSerializer):
        address = PersonAddressSerializer(many=True)

        class Meta:
            model = Person
            fields = (
                'id', 'first_name', 'last_name', 'age', 'gender', 'height', 'weight', 'phone_number', 'email',
                'address')
            extra_kwargs = {
                "id": {"read_only": True},
                "first_name": {"required": True,
                               "error_messages": {"required": "First name is required field.",
                                                  "blank": "First name is non blank field"}}
            }

    serializer_class = PersonSerializer
    permission_classes = (AllowAny,)
    http_method_names = ('get', 'post', 'put', 'delete')
    filter_backends = [QueryParamSchemaFilter, SearchFilter]
    filter_fields = ['address__city', 'address__state']
    search_fields = ['first_name', 'last_name']

    def get_param_fields(self, view):
        fields = [
            coreapi.Field(
                name='gender',
                required=False,
                location='query',
                description='',
                example='',
                type='',
            ),
            coreapi.Field(
                name='age',
                required=False,
                location='query',
                description='',
                example='',
                type='',
            ),
            coreapi.Field(
                name='height',
                required=False,
                location='query',
                description='',
                example='',
                type='',
            ),
            coreapi.Field(
                name='weight',
                required=False,
                location='query',
                description='',
                example='',
                type='',
            )
        ]
        return fields

    def get_queryset(self):
        return person_get_(self.request.query_params, self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request)
        if response.data:
            return Response({'data': response.data, 'message': 'success'},
                            status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = person_create_(request.data)
        if response:
            return Response(
                {
                    'data': self.serializer_class(response).data,
                    'message': 'success'
                }, status=status.HTTP_201_CREATED
            )

    def update(self, request, *args, **kwargs):

        try:
            person = Person.objects.get(id=kwargs['pk'])
            print(person)
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(serializer.data)
            response = person_update_(person, serializer.data)
            if response:
                serializer = self.serializer_class(response)
                return Response({
                    'data': serializer.data,
                    'message': 'success'}, status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return Response({'message': 'Person not found'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = Person.objects.get(id=kwargs['pk'])
            instance.delete()
            return Response({'message': 'success'}, status=status.HTTP_204_NO_CONTENT)
        except Person.DoesNotExist:
            return Response({'message': 'Person not found'}, status=status.HTTP_400_BAD_REQUEST)
