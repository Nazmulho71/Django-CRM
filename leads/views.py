from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # return HttpResponse("Hello Universe")
    return render(request, "leads/home_page.html")
