from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from itertools import chain
from operator import attrgetter
from . import models, forms


@login_required
def home(request):
    """Render the flux to the user"""
    # followers logic
    userfollow_followed = models.UserFollows.objects.filter(user=request.user)
    userfollowed = [userfollow.followed_user for userfollow in userfollow_followed]
    # Ticket logic
    tickets_followed = models.Ticket.objects.filter(user__in=userfollowed)
    tickets_user = models.Ticket.objects.filter(user=request.user)
    tickets_todisplay = list(chain(tickets_followed, tickets_user))
    tickets_reviewed = models.Ticket.objects.filter(review__isnull=False)
    # Review logic
    reviews_followed = models.Review.objects.filter(user__in=userfollowed)
    reviews_followers = models.Review.objects.filter(ticket__in=tickets_user)
    reviews_own = models.Review.objects.filter(user=request.user)
    reviews_todisplay = list(chain(reviews_followed, reviews_own))
    for review in reviews_followers:
        if review not in reviews_todisplay:
            reviews_todisplay.append(review)
    items = list(chain(reviews_todisplay, tickets_todisplay))
    items.sort(key=attrgetter("time_created"), reverse=True)
    user = request.user
    return render(
        request,
        "reviews/home.html",
        context={
            "tickets_todisplay": tickets_todisplay,
            "reviews_todisplay": reviews_todisplay,
            "items": items,
            "tickets_reviewed": tickets_reviewed,
            "user": user,
        },
    )


@login_required
def user_content(request):
    """Render the user personnal content page"""
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)
    tickets_reviewed = models.Ticket.objects.filter(review__isnull=False)
    return render(
        request,
        "reviews/user-content.html",
        context={
            "tickets": tickets,
            "reviews": reviews,
            "tickets_reviewed": tickets_reviewed,
        },
    )


@login_required
def ticket_upload(request):
    """Allow the creation of a ticket"""
    ticket_form = forms.TicketForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST)
        if ticket_form.is_valid():
            title = ticket_form.cleaned_data["title"]
            description = ticket_form.cleaned_data["description"]
            new_ticket = models.Ticket.objects.create(
                title=title,
                description=description,
                user=request.user,
            )
            new_ticket.save()
            return redirect("home")
    context = {"ticket_form": ticket_form}
    return render(request, "reviews/create_ticket.html", context=context)


@login_required
def review_upload(request, ticket_id):
    """Allow the creation off a review"""
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
    context = {"review_form": review_form, "ticket": ticket}
    return render(request, "reviews/create_review.html", context=context)


@login_required
def edit_review(request, review_id):
    """Allow the user to edit a review"""
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.EditReviewForm()
    delete_form = forms.DeleteReviewForm()
    if request.method == "POST":
        if "edit_review" in request.POST:
            edit_form = forms.EditReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect("home")
        if "delete_review" in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect("home")
    context = {"edit_form": edit_form, "delete_form": delete_form}
    return render(request, "reviews/edit_review.html", context=context)


@login_required
def create_reviewticket(request):
    """Allow user to create a review and a ticket simultaneously"""
    review_form = forms.ReviewForm()
    ticket_form = forms.TicketForm()
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        ticket_form = forms.TicketForm(request.POST)
        if review_form.is_valid() and ticket_form.is_valid():
            title = ticket_form.cleaned_data["title"]
            description = ticket_form.cleaned_data["description"]
            new_ticket = models.Ticket.objects.create(
                title=title,
                description=description,
                user=request.user,
            )
            new_ticket.save()
            rating = review_form.cleaned_data["rating"]
            headline = review_form.cleaned_data["headline"]
            body = review_form.cleaned_data["body"]
            new_review = models.Review.objects.create(
                rating=rating,
                headline=headline,
                body=body,
                ticket=new_ticket,
                user=request.user,
            )
            new_review.save()
            return redirect("home")
    context = {"review_form": review_form, "ticket_form": ticket_form}
    return render(request, "reviews/create-reviewticket.html", context=context)


@login_required
def edit_ticket(request, ticket_id):
    """Allow the edition of a ticket object"""
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.EditTicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == "POST":
        if "edit_ticket" in request.POST:
            edit_form = forms.EditTicketForm(request.POST, instance=ticket)
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


@login_required
def follow_user(request):
    """Allow the following of another user via the use of a UserFollows model's instance"""
    User = get_user_model()
    users = User.objects.all()
    userfollowsform = forms.UserFollowsForm()
    userfollowed = models.UserFollows.objects.filter(user=request.user)
    followers = models.UserFollows.objects.filter(followed_user=request.user)
    if request.method == "POST" and "follow" in request.POST:
        userfollowsform = forms.UserFollowsForm(request.POST)
        if userfollowsform.is_valid():
            lookedafter_user = userfollowsform.cleaned_data["User_to_follow"]
            for user in users:
                if user.username == lookedafter_user:
                    if (
                        userfollowed.filter(followed_user=user).exists()
                        or user == request.user
                    ):
                        return redirect("follow-user")
                    user_to_follow = user
                    new_userfollows = models.UserFollows.objects.create(
                        user=request.user, followed_user=user_to_follow
                    )
                    new_userfollows.save()
                    return redirect("follow-user")
            return redirect("follow-user")
    if request.method == "POST" and "unfollow" in request.POST:
        pass
    context = {
        "userfollowsform": userfollowsform,
        "userfollowed": userfollowed,
        "followers": followers,
    }
    return render(request, "reviews/follow-user.html", context=context)


@login_required
def delete_follow(request, id):
    """Unfollow a given user via deletion of the corresponding UserFollows instance"""
    models.UserFollows.objects.filter(id=id).delete()
    return redirect("follow-user")
