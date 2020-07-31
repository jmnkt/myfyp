from django.shortcuts import render, get_list_or_404, get_object_or_404
from .forms import UserProfileForm, GuideProfileForm, ItineraryModelForm, LicenseModelForm, ProfilePicModelForm
# from .models import User
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from .models import userProfile, profilePicImage, licenseFile, guideProfile
from rest_framework.permissions import IsAdminUser,AllowAny, IsAuthenticated
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def home(request):
    allUser = userProfile.objects.all()
    context = {"allUser" : allUser }
    return render(request, "home.html", context)

def userprofile_create(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST or None)
        profilePic_form = ProfilePicModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('profilePic')
        context = {
            "form" : form,
            "profilePic_form" : profilePic_form
            }
        
        if form.is_valid() and profilePic_form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.owner = user
            user_instance.save()
            form.save()
            for f in files:
                file_instance = profilePicImage(profilePic=f, userID=user_instance)
                file_instance.save()
    else:
        form = UserProfileForm()
        profilePic_form = ProfilePicModelForm()
        context = {
            "form" : form,
            "profilePic_form" : profilePic_form
            }
        if form.is_valid() and profilePic_form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.owner = user
            user_instance.save()
            form.save()
            for f in files:
                file_instance = profilePicImage(profilePic=f, userID=user_instance)
                file_instance.save()
                
    return render(request, "userCreateProfile.html", context)

def userprofile_detail(request, id):
    profileDetail= userProfile.objects.get(userID = id)
    # guideDetail= guideProfile.objects.get(user = id)
    
    context = {
        "profileDetail" : profileDetail,
        # "guideDetail" : guideDetail
        }
    return render(request, "profileDetail.html", context)

def guideprofile_create(request):
    user = request.user
    
    if request.method == 'POST':
        form = GuideProfileForm(request.POST or None)
        license_form = LicenseModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('licenses')
        context = {
            "form" : form,
            "license_form" : license_form,
            }
        if form.is_valid() and license_form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.user = user
            user_instance.save()
            form.save()
            for f in files:
                file_instance = licenseFile(licenses=f, guideID=user_instance)
                file_instance.save()
    else:
        form = GuideProfileForm()
        license_form = LicenseModelForm()
        context = {
            "form" : form,
            "license_form" : license_form
            }
        if form.is_valid() and license_form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.user = user
            user_instance.save()
            form.save()
            for f in files:
                file_instance = licenseFile(licenses=f, guideID=user_instance)
                file_instance.save()
                
    return render(request, "guideCreateProfile.html", context)
   
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user-profile-create')
    else:
        form = UserCreationForm()
    return render(request, 'signUp.html', {'form': form})

def guide_based_on_state(request, id):
    guide_list = guideProfile.objects.filter(guidingState = id)
    context = {
        "guide_list": guide_list
    }
    return render(request, "listAllGuide.html", context)

def guide_browse(request, id):
    guide_list = guideProfile.objects.filter(guidingState = id)
    context = {
        "guide_list": guide_list
    }
    return render(request, "browseAllGuide.html", context)

def guideprofile_detail_travelers(request, id):
    profileDetail= guideProfile.objects.get(user = id)
    context = {"profileDetail" : profileDetail}
    return render(request, "guideProfileDetailForTravelers.html", context)

def guideprofile_detail(request, id):
    profileDetail= guideProfile.objects.get(user = id)
    context = {"profileDetail" : profileDetail}
    return render(request, "guideProfileDetail.html", context)

def browse_guideprofile_detail(request, id):
    profileDetail= guideProfile.objects.get(user = id)
    context = {"profileDetail" : profileDetail}
    return render(request, "browseGuideProfileDetail.html", context)
