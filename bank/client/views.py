from django.shortcuts import render
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from .models import ClientInfo, ClientStaff, ContactInfo
from .serializers import ClientSerializer, ContactSerializer

# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):

    queryset = ClientInfo.objects.all()
    serializer_class = ClientSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status_code": 0,
            "data": serializer.data,
        },
            status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        print(instance.clientaccount_set.all())
        if (instance.clientaccount_set.all()) or (instance.loaninfo_set.all()):  # Have Account
            print("This client cannot be deleted.")
            return Response({
                'status_code': -1,
                'msg': "This client has client. Cannot delete.",
            },
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            instance.delete()
            return Response({
                "status_code": 0,
                "msg": "Deleted Successfully.",
            },
                status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({
            "status_code": 0,
            "data": serializer.data
        },  status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "status_code": 0,
            "data": serializer.data
        },
            status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status_code': 0,
            'data': serializer.data
        },
            status=status.HTTP_201_CREATED, headers=headers)


class ContactViewSet(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    queryset = ContactInfo.objects.all()
    serializer_class = ContactSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'status_code': 0,
            'data': serializer.data
        },
            status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status_code': 0,
            'data': serializer.data
        },
            status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.clientinfo_set.all():
            print(instance.clientinfo_set.all())
            return Response(
                {
                    'status_code': -1,
                    'msg': "This contact is related to some client. Please remove relation first."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        self.perform_destroy(instance)
        return Response({
            'status_code': 0
        },
            status=status.HTTP_204_NO_CONTENT)
