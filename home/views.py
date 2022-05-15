from django.shortcuts import render

# Create your views here.


def index(request):
    """ View that renders the index page """
    return render(request, 'home/index.html')