from rest_framework import serializers
from django.apps import apps

#Convert itinerary model to JSON
class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('itineraries.Itinerary')
        fields = '__all__'