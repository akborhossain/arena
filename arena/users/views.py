from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import LoginForm
from events.models import Event

# Create your views here.
class Dashboard(View):
    template_name='users/dashboard.html'
    @method_decorator(login_required(login_url='user_login'))
    def get(self, request):
            return render(request, self.template_name)

class EventListView(View):
    template_name = 'events/eventlist.html'

    @method_decorator(login_required(login_url='user_login'))
    def get(self, request):
        # Retrieve tasks for the currently logged-in user
        event = Event.objects.filter(username=request.user)
        
        context = {
            'events': event
        }

        return render(request, self.template_name, context)

class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')  
        # Display the login form
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')  
        # Process the login form data
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a page after successful login
                return redirect('dashboard')
            else:
                # Handle authentication failure
                return render(request, self.template_name, {'form': form, 'error': 'Invalid login credentials'})
        return render(request, self.template_name, {'form': form})
    

class LogoutView(View):

    @method_decorator(login_required(login_url='user_login'))
    def get(self, request):
        logout(request)
        return redirect('user_login')
