from rest_framework import serializers
from django.apps import apps

#Convert Reward model to JSON
class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('itineraries.Reward')
        fields = '__all__'

#Convert Itinerary model to JSON
class ItinerarySerializer(serializers.ModelSerializer):
    rewards = RewardSerializer(many=True, read_only=True) #serialized list of rewards related to itinerary
    
    class Meta:
        model = apps.get_model('itineraries.Itinerary')
        fields = '__all__'

