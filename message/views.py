from django.shortcuts import render
from .forms import messageToGuideForm, messageToTravelerForm
from trips.models import tripGuide
from .models import messageToTraveler, messageToGuide

def sendGuideMessage(request, id):
    user = request.user
    trip = tripGuide.objects.get( tripID = id )
    form = messageToGuideForm(request.POST or None)
   
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
            
    return render(request, 'createNewMessage.html', context)

def sendTravelerMessage(request, id):
    user = request.user
    trip = tripGuide.objects.get( tripID = id )
    form = messageToTravelerForm(request.POST or None)
   
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
            
    return render(request, 'createNewMessage.html', context)

def traveler_message_received(request):
    id = request.user.id
    message_list = messageToTraveler.objects.filter(recipientID = id)
    context = {
        "message_list": message_list
    }
    return render(request, "listAllMessagesToTravelers.html", context)

def guide_message_received(request, id):
    message_list = messageToGuide.objects.filter(recipientID = id)
    context = {
        "message_list": message_list
    }
    return render(request, "listAllMessagesToGuides.html", context)

def guide_message_received_detail(request, id):
    message = messageToGuide.objects.get(messagesID = id)
    context = {
        "message": message
    }
    return render(request, "listMessageToGuideDetail.html", context)

def traveler_message_received_detail(request, id):
    message = messageToTraveler.objects.get(messagesID = id)
    context = {
        "message": message
    }
    return render(request, "listMessageToTravelerDetail.html", context)