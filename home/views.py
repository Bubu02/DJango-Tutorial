from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }

    # return HttpResponse("This is homepage.")
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("This is about page.")

def contact(request):
    return HttpResponse("This is contact page.")

def service(request):
    return HttpResponse("This is service page.")
