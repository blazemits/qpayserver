from rest_framework import serializers
from SignUp.models import wallet_table,bank_table,user_table






class Bank_Serializer(serializers.ModelSerializer):
    class Meta:
        model=bank_table
        field='__all__'
        #('bank_ac_num','bank_ifci_code','user_status')

class Wallet_Serializer(serializers.ModelSerializer):
    bank_ac_num=Bank_Serializer(read_only=True)
    class Meta:
        model=wallet_table
        field='__all__'

class   User_Serializer(serializers.ModelSerializer):
    mob_num=Wallet_Serializer(read_only=True)
    class Meta:
        model=user_table
        field='__all__'
