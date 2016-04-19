from rest_framework import serializers
from login_app.models import Login_Model



class   Login_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Login_Model
        field=('id','name','pwd')