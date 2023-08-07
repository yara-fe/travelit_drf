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


class Reward(models.Model):
    amount = models.IntegerField
    giver = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    itinerary_id = models.ForeignKey(
        'Itinerary', #model whic Reward is related to
        on_delete=models.CASCADE, #delete Rewards if Itinerary is deleted
        related_name='rewards' #allows Django to set up a "property" in Itinerary model
    )
    comment = models.CharField(max_length=200)
    reward_date = models.DateTimeField()