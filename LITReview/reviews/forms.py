from collections import UserList
from dataclasses import fields
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

# blog/forms.py
from django.contrib.auth import get_user_model


from . import models

STATUSCHOICES = (
    (1, ("*")),
    (2, ("**")),
    (3, ("***")),
    (4, ("****")),
    (5, ("*****")),
)


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ["title", "description", "user"]


class ReviewForm(forms.Form):
    rating = forms.ChoiceField(
        choices=STATUSCHOICES,
        label="",
        initial="",
        widget=forms.Select(),
        required=True,
    )
    headline = forms.CharField(max_length=128)
    body = forms.CharField(
        widget=forms.Textarea(attrs={"name": "body", "rows": "5", "cols": "33"})
    )


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


User = get_user_model()
Users = User.objects.all()


class UserFollowsForm(forms.Form):
    User_to_follow = forms.ModelChoiceField(queryset=User.objects.all())
