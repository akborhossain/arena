from django.contrib import admin
from django.urls import path
from .views import LoginView, LogoutView, EventListView,Dashboard, UserRegistrationView

urlpatterns = [
        path('',LoginView.as_view(),name='user_login'),
        path('logout/',LogoutView.as_view(), name='logout'),
        path('events/',EventListView.as_view(),name='events'),
        path('dashboard/',Dashboard.as_view(),name='dashboard'),
        path('signup/',UserRegistrationView.as_view(), name='signup'),

]