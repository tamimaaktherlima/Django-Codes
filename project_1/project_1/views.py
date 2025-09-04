from django.http import HttpResponse

def home(request):
    return HttpResponse("This is My HOME Page")
def contact(resquest):
    return HttpResponse("This is my Contact Page")