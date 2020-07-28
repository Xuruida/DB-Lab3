from rest_framework import serializers
from .models import BranchInfo

class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = BranchInfo
        fields = 'all'
