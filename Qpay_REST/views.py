from django.http import HttpResponse


def home(request):
    return HttpResponse("Qpay Home page \n Test By JpG ")

def api_page(request):
    return HttpResponse("Qpay api_page \n Test By JpG ")