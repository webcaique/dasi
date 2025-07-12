from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *args, **kargs):
    context = {
        "text":"A text",
        "number": 123,
    }
    return render(request, "index.html", context)