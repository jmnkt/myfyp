from django.shortcuts import render
from .forms import UserForm

def create_user_profile(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "profile_create.html", context)
