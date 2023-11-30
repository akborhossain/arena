from django.contrib import admin
from django.urls import path
from .views import LoginView, LogoutView, EventListView,Dashboard

urlpatterns = [
        path('',LoginView.as_view(),name='user_login'),
        path('logout/',LogoutView.as_view(), name='logout'),
        path('events/',EventListView.as_view(),name='events'),
        path('dashboard/',Dashboard.as_view(),name='dashboard'),

]