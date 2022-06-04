from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from user_management import models, forms


# Helper functions
def extract_user_from_valid_form(request: HttpRequest) -> models.User | forms.UserForm:
    form = forms.UserForm(request.POST)
    if form.is_valid():
        return form.save(commit=False)
    else:
        return form


# Create your views here.
def author_signup(request: HttpRequest):
    # Form submitted
    if request.method == 'POST':
        user = extract_user_from_valid_form(request)
        # If form was returned instead of user, form contains errors
        if isinstance(user, forms.UserForm):
            return render(request, 'user_management/author_signup_form.html', context={'form': user})
        # Else the form was valid
        else:
            # Save the user and it's corresponding author
            user.save()
            author = models.Author(user=user)
            author.save()
            # Return success page
            return render(request, 'user_management/signup_success.html')
    # Form requested
    else:
        return render(request, 'user_management/author_signup_form.html', context={'form': forms.UserForm})


def reader_signup(request: HttpRequest):
    pass
