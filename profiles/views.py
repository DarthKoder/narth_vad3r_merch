from django.shortcuts import render, get_list_or_404
from allauth.account.views import ConfirmEmailView

from .models import UserProfile


def profile(request):
    """ Display the user's profile. """
    profile = get_list_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)

class CustomConfirmEmailView(ConfirmEmailView):
    template_name = 'email.html'
    pass
