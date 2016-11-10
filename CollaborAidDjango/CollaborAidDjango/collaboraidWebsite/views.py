from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse

from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from collaboraidWebsite.forms import AuthenticationForm, RegistrationForm




def index(request):
    """
    Return a list of stories that match the provided search term
    in either the title or the main content.
    """
    return HttpResponse("Hello, world. You're at the polls index.")
#    return render_to_response("index.html", {}, RequestContext(request))


def login(request):
    """
    Log in view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/')
    else:
        form = AuthenticationForm()
    return render_to_response('collaboraidDjango/templates/login.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def register(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render_to_response('collaboraidDjango/templates/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect('/')