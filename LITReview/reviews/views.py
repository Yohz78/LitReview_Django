from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from . import models, forms


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    return render(
        request,
        "reviews/home.html",
        context={
            "tickets": tickets,
            "reviews": reviews,
        },
    )


@login_required
def ticket_upload(request):
    ticket_form = forms.TicketForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket_form.save()
            return redirect("home")
    context = {"ticket_form": ticket_form}
    return render(request, "reviews/create_ticket.html", context=context)


@login_required
def review_upload(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            rating = review_form.cleaned_data["rating"]
            headline = review_form.cleaned_data["headline"]
            body = review_form.cleaned_data["body"]
            new_review = models.Review.objects.create(
                rating=rating,
                headline=headline,
                body=body,
                ticket=ticket,
                user=request.user,
            )
            new_review.save()
            return redirect("home")
    context = {"review_form": review_form}
    return render(request, "reviews/create_review.html", context=context)


@login_required
def follow_user(request):
    userfollowsform = forms.UserFollowsForm()
    if request.method == "POST":
        userfollowsform = forms.UserFollowsForm(request.POST)
        if userfollowsform.is_valid():
            user_to_follow = userfollowsform.cleaned_data["User_to_follow"]
            new_userfollows = models.UserFollows.objects.create(
                user=request.user, followed_user=user_to_follow
            )
            new_userfollows.save()
            return redirect("home")
    context = {"userfollowsform": userfollowsform}
    return render(request, "reviews/follow-user.html", context=context)


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == "POST":
        if "edit_ticket" in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect("home")
        if "delete_ticket" in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect("home")

    context = {"edit_form": edit_form, "delete_form": delete_form}
    return render(request, "reviews/edit_ticket.html", context=context)
