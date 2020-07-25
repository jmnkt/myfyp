from django.shortcuts import render
from .forms import ReviewsForGuidesForm, ReviewsForTravelersForm
from trips.models import tripGuide
from .models import ReviewsForTravelers, ReviewsForGuides

def leaveGuideReview(request, id):
    user = request.user
    trip = tripGuide.objects.get( tripID = id )
    form = ReviewsForGuidesForm(request.POST or None)
   
    context = {
        'trip' : trip,
        'form' : form
    }
    
    if form.is_valid():
        instance = form.save(commit = False)
        instance.senderID = user
        instance.tripID = trip.tripID.tripID
        instance.recipientID = trip.guides.guidesID
        instance.save()
        form.save()
            
    return render(request, 'createNewReview.html', context)

def leaveTravelerReview(request, id):
    user = request.user
    trip = tripGuide.objects.get( tripID = id )
    form = ReviewsForTravelersForm(request.POST or None)
   
    context = {
        'trip' : trip,
        'form' : form
    }
    
    if form.is_valid():
        instance = form.save(commit = False)
        instance.senderID = user
        instance.tripID = trip.tripID.tripID
        instance.recipientID = trip.tripID.user.id
        instance.save()
        form.save()
            
    return render(request, 'createNewReview.html', context)

def traveler_review_received(request):
    id = request.user.id
    review_list = ReviewsForTravelers.objects.filter(recipientID = id)
    context = {
        "review_list": review_list
    }
    return render(request, "listAllReviewsToTravelers.html", context)

def guide_review_received(request, id):
    review_list = ReviewsForGuides.objects.filter(recipientID = id)
    context = {
        "review_list": review_list
    }
    return render(request, "listAllReviewsToGuides.html", context)