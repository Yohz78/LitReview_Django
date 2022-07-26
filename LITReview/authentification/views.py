from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.conf import settings

from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "authentification/signup.html", context={"form": form})
