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


# def logout_user(request):

#     logout(request)
#     return redirect("login")


# class LoginPage(View):
#     form_class = forms.LoginForm
#     template_name = "authentification/login.html"

#     def get(self, request):
#         form = self.form_class
#         message = ""
#         return render(
#             request,
#             self.template_name,
#             context={"form": form, "message": message},
#         )

#     def post(self, request):
#         form = self.form_class(request.POST)
#         message = ""
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data["username"],
#                 password=form.cleaned_data["password"],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect("home")
#             else:
#                 message = "Invalid credentials"
#         return render(
#             request,
#             self.template_name,
#             context={"form": form, "message": message},
#         )