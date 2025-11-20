from django.http import HttpResponse

def client_home(request):
    return HttpResponse("Welcome to the Clients app!")
