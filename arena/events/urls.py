from django.contrib import admin
from django.urls import path
from .views import CreateTaskView,EventDetailsView, EventRegister,MyEventListView,EventUnregister

urlpatterns = [
    path('create/',CreateTaskView.as_view(),name='create'),
    path('event/<int:id>/', EventDetailsView.as_view(), name='singleevent'),
    path('event/<int:event_id>/register/', EventRegister.as_view(), name='register'),
    path('myevent/', MyEventListView.as_view(), name='myevent'),
    path('event/<int:event_id>/unregister/', EventUnregister.as_view(), name='unregister'),



   
]