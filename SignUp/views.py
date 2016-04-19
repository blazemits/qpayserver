from rest_framework import viewsets
from SignUp.serializers import Bank_Serializer,Wallet_Serializer,User_Serializer
from SignUp.models import wallet_table,bank_table,user_table

"""
class main_view(viewsets.ModelViewSet):
    queryset =bank_table.objects.all()
    serializer_class = Bank_Serializer


    """

class Wallet_View_Sets(viewsets.ModelViewSet):
        queryset = wallet_table.objects.all()
        serializer_class = Wallet_Serializer


class Bank_View_Sets(viewsets.ModelViewSet):
        queryset = bank_table.objects.all()
        serializer_class = Bank_Serializer


class User_View_Sets(viewsets.ModelViewSet):
        queryset = user_table.objects.all()
        serializer_class = User_Serializer