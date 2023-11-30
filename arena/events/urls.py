from django.contrib import admin
from django.urls import path
from .views import CreateTaskView,EventDetailsView, EventRegister

urlpatterns = [
    path('create/',CreateTaskView.as_view(),name='create'),
    path('event/<int:id>/', EventDetailsView.as_view(), name='singleevent'),
    path('event/<int:event_id>/register/', EventRegister.as_view(), name='register'),


   
]