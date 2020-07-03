from rest_framework import serializers

from .models import ClientInfo, ClientStaff

class ClientSerializer(serializers.ModelSerializer):
    """
    List Clients Serializer.
    """

    class Meta:
        model = ClientInfo
        fields = '__all__'