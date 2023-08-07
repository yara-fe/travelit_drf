from django.db import models

class Itinerary(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audience = models.TextField()
    cost = models.TextField()
    travel_date = models.TextField()
    location = models.TextField()
    itinerary_notes = models.TextField()
    image = models.URLField()
    date_created = models.DateTimeField()
    creator = models.CharField(max_length=200) #user who created the itinerary
