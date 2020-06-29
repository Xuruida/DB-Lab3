from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import SavingsSerializer, CheckingSerializer
from .models import AccountBase, SavingsAccountInfo, CheckingAccountInfo
# Create your views here.

class SavingsViewSet(viewsets.ModelViewSet):

    serializer_class = SavingsSerializer
    queryset = SavingsAccountInfo.objects.all()

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['account_base']['is_savings'] = True
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status_code': 0,
            'data': serializer.data
        },
            status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        print(instance.account_base.account_ID)

        # destroy two instances
        self.perform_destroy(instance)
        self.perform_destroy(instance.account_base)
        return Response({
            "status_code": 0,
            "msg": "Deleted Successfully.",
        },
            status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        print("Updating:... ", serializer.validated_data)
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

class CheckingViewSet(viewsets.ModelViewSet):
    
    serializer_class = CheckingSerializer
    queryset = CheckingAccountInfo.objects.all()
    
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['account_base']['is_savings'] = True
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status_code': 0,
            'data': serializer.data
        },
            status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        print(instance.account_base.account_ID)
        self.perform_destroy(instance)
        self.perform_destroy(instance.account_base)
        return Response({
            "status_code": 0,
            "msg": "Deleted Successfully.",
        },
            status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        print("Updating:... ", serializer.validated_data)
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