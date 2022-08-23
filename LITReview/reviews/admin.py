from django.contrib import admin

from .models import Review, Ticket, UserFollows
from authentification.models import User

admin.site.register(Review)
admin.site.register(Ticket)
admin.site.register(UserFollows)
admin.site.register(User)
