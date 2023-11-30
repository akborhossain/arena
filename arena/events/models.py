from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Import User model

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    event_time= models.DateField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.username.is_superuser:
            raise ValidationError("Non-superusers are not allowed to create events.")

        # Check if there is already an event on the same date for a non-superuser
        events_on_same_date = Event.objects.filter(event_time=self.event_time).exclude(pk=self.pk)
        if events_on_same_date.exists():
            raise ValidationError("Only one event is allowed per day.")

        # Check if there is already an event on the same date for a superuser
        if self.username.is_superuser:
            super_events_on_same_date = Event.objects.filter(event_time=self.event_time).exclude(pk=self.pk)
            if super_events_on_same_date.exists():
                raise ValidationError("Superusers are limited to one event per day as well.")

        super().save(*args, **kwargs)


class EventRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    eid = models.IntegerField()
    registration_at = models.DateTimeField(default=timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        # Add a unique constraint to ensure a user can only register once for an event
        unique_together = ('eid', 'username',)

