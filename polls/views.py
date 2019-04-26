from django.http import HttpResponse

def index(request):
    return HttpResponse("hello i am riju")
