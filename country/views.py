from django.shortcuts import render
from .models import Country, State

def country_list(request):
    country = Country.objects.all()
    context = {
        "country_list": country
    }
    return render(request, "listAllCountry.html", context)

def country_browse(request):
    country = Country.objects.all()
    context = {
        "country_list": country
    }
    return render(request, "browseAllCountry.html", context)

def state_browse(request, country):
    state = State.objects.filter(country = country)
    context = {
        "state_list": state
    }
    return render(request, "browseAllState.html", context)

def state_based_on_country(request, country):
    state = State.objects.filter(country = country)
    context = {
        "state_list": state
    }
    return render(request, "listAllState.html", context)
    