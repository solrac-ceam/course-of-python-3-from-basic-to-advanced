from django.shortcuts import render


# Create your views here.
def index(request):
    print("Home page accessed")
    context = {"text": "We are in Home"}
    return render(request, "home/index.html", context)
