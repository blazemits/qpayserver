from rest_framework import viewsets
from login_app.serializers import Login_Serializer
from login_app.models import Login_Model



class Login_View_Sets(viewsets.ModelViewSet):
    queryset = Login_Model.objects.all()
    serializer_class = Login_Serializer