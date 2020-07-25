from django.shortcuts import render
from .forms import tripDetailsForm, tripGuideForm, tripGuideFormForGuide
from .models import Trip, tripGuide
from profiles.models import guideProfile

def trip_create(request):
    user = request.user
    form = tripDetailsForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = user
        instance.save()
        form.save()
    context = {"form": form}
    return render(request, "createNewTrip.html", context)

def trip_based_on_traveler(request, id):
    trips = Trip.objects.filter(user = id)
    context = {
        "trips": trips
    }
    return render(request, "listUpcomingTrip.html", context)

def trip_detail(request, id):
    trips = Trip.objects.get(tripID = id)
    context = {
        "trips": trips
    }
    return render(request, "listTripDetail.html", context)

def trip_detail_guides(request, id):
    trips = Trip.objects.get(tripID = id)
    context = {
        "trips": trips
    }
    return render(request, "listTripDetailForGuides.html", context)

def trip_based_on_guide(request, id):
    trips = tripGuide.objects.filter(guides = id)
    context = {
        "trips": trips
    }
    return render(request, "listIncomingTrip.html", context)

def trip_update_guide(request, id):
    trips = tripGuide.objects.get(tripID = id)
    form = tripGuideFormForGuide(request.POST or None, instance=trips)
    context = {
        "trips": trips,
        "form": form
    }
    if form.is_valid():
        form.save()
    return render(request, "updateIncomingTripDetails.html", context)

def select_guide(request, id):
    guides = guideProfile.objects.get(guidesID = id)
    form = tripGuideForm(request.POST or None)
    context = {
            "guide": guides,
            "form": form
        }
    if form.is_valid():
        form.save()
    return render(request, "selectGuide.html", context)

def trip_status(request, id):
    trips = tripGuide.objects.get(tripID = id)
    context = {
        "trips": trips
    }
    return render(request, "listTripStatus.html", context)