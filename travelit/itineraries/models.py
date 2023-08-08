from django.db import models
from django.contrib.auth import get_user_model #reference to user model

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
    #user who created the itinerary
    creator = models.ForeignKey(
        get_user_model(), #related model
        on_delete=models.CASCADE,
        related_name='owned_itineraries' #sets up property in get_user_model
    ) 


class Reward(models.Model):
    amount = models.IntegerField
    giver = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='rewards'
    ) 
    anonymous = models.BooleanField()
    itinerary_id = models.ForeignKey(
        'Itinerary', #model which Reward is related to
        on_delete=models.CASCADE, #delete Rewards if Itinerary is deleted
        related_name='rewards' #allows Django to set up a "property" in Itinerary model
    )
    comment = models.CharField(max_length=200)
    reward_date = models.DateTimeField()