from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import get_object_or_404
from .forms import EventForm
from .models import EventRegistration, Event

# Create your views here.


from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

class CreateTaskView(View):
    template_name = 'events/create.html'

    @method_decorator(login_required(login_url='user_login'))
    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='access_denied'))
    def get(self, request):
        form = EventForm()
        return render(request, self.template_name, {'form': form})

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='access_denied'))
    def post(self, request):
        if not request.user.is_superuser:
            messages.error(request, "You are not permitted to create events.")
            return redirect('access_denied')  # Redirect to an access denied page or any other page you prefer

        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)  # Create the task object but don't save it yet
            event.username = request.user  # Set the username field
            event.save()  # Now save the task with the username
            messages.success(request, "Event created successfully.")
            return redirect('events')  # Redirect to the task list view

        # If form is not valid, render the form with errors
        return render(request, self.template_name, {'form': form})

class EventDetailsView(View):
    template_name = 'events/singleevent.html'

    @method_decorator(login_required(login_url='user_login'))
    def get(self, request, id):
        event = get_object_or_404(Event, id=id)
        return render(request, self.template_name, {'event': event})

    @method_decorator(login_required(login_url='user_login'))
    def post(self, request, id):
        event = get_object_or_404(Event, id=id)

        if request.method == 'POST':
            return redirect('singleevent', id=id)
        


class EventRegister(View):
    @method_decorator(login_required(login_url='user_login'))
    def get(self, request, event_id):
        # Handle GET request, you can render a template if needed
        event = Event.objects.get(pk=event_id)
        return render(request, 'events/register.html', {'event': event})

    @method_decorator(login_required(login_url='user_login'))
    def post(self, request, event_id):
        # Handle POST request for event registration

        # Check if the user has already registered for the event
        user = request.user
        event = Event.objects.get(pk=event_id)
        existing_registration = EventRegistration.objects.filter(eid=event_id, username=user)

        if existing_registration.exists():
            # User has already registered for this event
            messages.warning(request, 'You have already registered for this event.')
            return redirect('singleevent', id=event_id)
        # Create a new registration for the user and event
        if not existing_registration.exists():
            registration = EventRegistration(eid=event_id, username=user)
            registration.save()
        # Optionally, you can add more logic here, such as sending confirmation emails, etc.

        messages.success(request, 'Successfully registered for the event!')
        return redirect('singleevent', id=event_id)
