from django.http import HttpResponse


def home(request):
   
    return HttpResponse("Just testing if logging works")