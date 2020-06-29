from rest_framework import serializers

from .models import ClientInfo, ContactInfo, ClientStaff

class ClientSerializer(serializers.ModelSerializer):
    """
    List Clients Serializer.
    """

    contact_name = serializers.ReadOnlyField(source='contact.name')
    contact_tel = serializers.ReadOnlyField(source="contact.tel")
    contact_email = serializers.ReadOnlyField(source="contact.email")

    class Meta:
        model = ClientInfo
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    """
    Contact Serializer.
    """

    class Meta:
        model = ContactInfo
        fields = '__all__'