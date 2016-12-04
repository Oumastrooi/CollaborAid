from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from website.models import UserProfile, AnEvent
from website.forms import UserProfileForm, AnEventForm, SearchForm
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import render_to_response
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    response = render(request, 'website/index.html')
    
    return response
    

def about(request):
    return render(request, 'website/about.html',{})
    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
    else:    	
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'website/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered
                  })

@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            
            return redirect('index')
        else:
            print(form.errors)

    context_dict = {'form':form}
    
    return render(request, 'website/profile_registration.html', context_dict)

class WebsiteRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')

@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
    
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'first_name': userprofile.first_name, 'last_name': userprofile.last_name, 
                            'picture': userprofile.picture })
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)
    
    return render(request, 'website/profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})

@login_required
def register_event(request):
    form = AnEventForm()
    if request.method == 'POST':
        form = AnEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('created_event')
        else:
            print(form.errors)

    context_dict = {'form':form}
    
    return render(request, 'website/event_registration.html', context_dict)

@login_required
def join(request, event_id):
    try:
        # already joined
        event = AnEvent.objects.get(id=event_id, volunteer=request.user)
        message = "You have already joined this event"
    except AnEvent.DoesNotExist as e:
        # Event exists and join
        try:
            event = AnEvent.objects.get(id=event_id)
            event.volunteer.add(request.user)
            event.save()
            message = "You have joined this event"
        except AnEvent.DoesNotExist as e:
            message = "Error on event joining"

    event = AnEvent.objects.get(id=event_id)
    joined = event.volunteer.filter(id=request.user.id)
    return render(request, 'website/event_details.html', {
       'event': event,
       'message': message,
       'joined': joined
    })

@login_required
def cancel(request, event_id):
    try:
        event = AnEvent.objects.get(id=event_id, volunteer=request.user)
        event.volunteer.remove(request.user)
        event.save()
        message = "Your request not to attend has been saved"
    except AnEvent.DoesNotExist as e:
           message = "Error on cancelling your attedance on event"

    event = AnEvent.objects.get(id=event_id)
    joined = event.volunteer.filter(id=request.user.id)
    return render(request, 'website/event_details.html', {
        'event': event,
        'message': message,
        'joined': joined
    })

@login_required
def event_complete(request):
    response = render(request, 'website/creation_complete.html')
    
    return response
    
@login_required
def list_profiles(request):
    userprofile_list = UserProfile.objects.all()
    return render(request, 'website/list_profiles.html', { 'userprofile_list' : userprofile_list})

def list_events(request):
    event_list = AnEvent.objects.all()
    return render(request, 'website/list_events.html', { 'event_list' : event_list})
    
    #this currently displays NEW upcoming events
    #if no new events, then empty
    #try:
    #    event = AnEvent.objects.filter(date__gt=datetime.now()).order_by('date')
    #except:
    #    event = []
        
    return render(request, 'website/list_events.html', {'event': event})

# Provides individual event details
@login_required
def detail(request, id):
   event = AnEvent.objects.get(id=id)
   joined = event.volunteer.filter(id=request.user.id)
   return render(request, 'website/event_details.html', {'event': event, 'joined': joined})

# helper functions
def search_by_event_name(query):
    results = AnEvent.objects.filter(event_name__icontains=query)
    return results

def search_by_username(query):
    results = UserProfile.objects.filter(user__icontains=query)
    return results

def search_by_address(query):
    results = AnEvent.objects.filter(address__icontains=query)
    return results

def search_by_venue(query):
    results = AnEvent.objects.filter(venue__icontains=query)
    return results

@login_required
def search(request):
    if request.method == 'GET':
        return render(request, 'website/search.html')
    else:
        # validate submitted form
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            parameter = form.cleaned_data['parameter']

            if parameter == 'Event Name' and query is not None:
                res = search_by_event_name(query)
                return render(request, 'website/results.html', {'query': query, 'results': res})
            elif parameter == 'Username' and query is not None:
                res = search_by_username(query)
                return render(request, 'website/results.html', {'query': query, 'results': res})
            elif parameter == 'Address' and query is not None:
                res = search_by_address(query)
                return render(request, 'website/results.html', {'query': query, 'results': res})
            elif parameter == 'Venue' and query is not None:
                res = search_by_venue(query)
                return render(request, 'website/results.html', {'query': query, 'results': res})
            else:
                messages.error(request, 'Invalid search entry.')
                return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Invalid search entry.')
            return HttpResponseRedirect('/')
