from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers,viewsets,serializers
from Qpay_REST.views import home, api_page
from SignUp.views import Bank_View_Sets,User_View_Sets,Wallet_View_Sets
from login_app.views import Login_View_Sets



#Routers
Main_router = routers.SimpleRouter()
Main_router.register(r'login', Login_View_Sets)
Main_router.register(r'signup/bank',Bank_View_Sets)
Main_router.register(r'signup/wallet',Wallet_View_Sets)
Main_router.register(r'signup/user',User_View_Sets)


urlpatterns = [
    url(r'^$',home),
    url(r'^api/$',api_page),
    url(r'^api/', include(Main_router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
