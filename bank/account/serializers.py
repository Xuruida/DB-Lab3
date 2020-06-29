from rest_framework import serializers

from .models import AccountBase, CheckingAccountInfo, SavingsAccountInfo, ClientAccount

from .models import LoanInfo, ReleaseInfo

class CASerializer(serializers.ModelSerializer):
    """
    Client Account
    """

    class Meta:
        model = ClientAccount
        fields = '__all__'

class AccountBaseSerializer(serializers.ModelSerializer):
    """
    Account Base Serializer.
    """

    class Meta:
        model = AccountBase
        fields = ['account_ID', 'open_date', 'is_savings']

class CheckingSerializer(serializers.ModelSerializer):
    
    account_base = AccountBaseSerializer()

    def create(self, validated_data):
        """
        implement create method

        reference: rest_framework/serializers.py
        """
        account_data = validated_data.pop('account_base')
        account_data['is_savings'] = False
        print(validated_data, account_data, sep='\n')
        base = AccountBase.objects.create(**account_data) # AccountBase
        ck = CheckingAccountInfo.objects.create(account_base=base, **validated_data) # Savings
        return ck

    def update(self, instance, validated_data):
        """
        implement update method.

        reference: rest_framework/serializers.py
        """
        account_data = validated_data.pop('account_base')
        account_data['is_savings'] = False
        print(validated_data, account_data, sep='\n')
        # checking's data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        for attr, value in account_data.items():
            setattr(instance.account_base, attr, value)

        return instance

    class Meta:
        model = CheckingAccountInfo
        fields = '__all__'

class SavingsSerializer(serializers.ModelSerializer):

    account_base = AccountBaseSerializer()

    def create(self, validated_data):
        """
        implement create method

        reference: rest_framework/serializers.py
        """
        account_data = validated_data.pop('account_base')
        account_data['is_savings'] = True
        print(validated_data, account_data, sep='\n')
        base = AccountBase.objects.create(**account_data) # AccountBase
        sv = SavingsAccountInfo.objects.create(account_base=base, **validated_data) # Savings
        return sv

    def update(self, instance, validated_data):
        """
        implement update method.

        reference: rest_framework/serializers.py
        """
        account_data = validated_data.pop('account_base')
        account_data['is_savings'] = True
        print(validated_data, account_data, sep='\n')
        # savings's data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        for attr, value in account_data.items():
            setattr(instance.account_base, attr, value)

        return instance

    class Meta:
        model = SavingsAccountInfo
        fields = '__all__'

class ReleaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReleaseInfo
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanInfo
        fields = ['loan_ID', 'branch', 'total_amount', 'clients']

