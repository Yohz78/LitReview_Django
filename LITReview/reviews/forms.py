from dataclasses import fields
from django import forms

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
    """Form gathering all necessary ticket information"""

    # edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ["title", "description"]


class ReviewForm(forms.Form):
    """Form gathering all necessary review information"""

    # class Meta:
    #     model = models.Review
    #     fields = ["rating", "headline", "body"]

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
    """Allow deletion of a ticket"""

    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeleteReviewForm(forms.Form):
    """Allow deletion of a review"""

    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeleteFollowForm(forms.Form):
    """Allow unsucribing from given user"""

    delete_follow = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class EditTicketForm(forms.ModelForm):
    """Allow the edition of a ticket"""

    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ["title", "description"]


class EditReviewForm(forms.ModelForm):
    """Allow the edition of a review"""

    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ["rating", "headline", "body"]

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


class UserFollowsForm(forms.Form):
    User_to_follow = forms.CharField()
