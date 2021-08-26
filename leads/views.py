from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


def home_page(request):
    # return HttpResponse("Home page")
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request, "second_page.html", context)