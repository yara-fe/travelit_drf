from rest_framework import serializers
from django.apps import apps

#Convert Reward model to JSON
class RewardSerializer(serializers.ModelSerializer):
    giver = serializers.ReadOnlyField(source='giver.id')
    class Meta:
        model = apps.get_model('itineraries.Reward')
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.giver = validated_data.get('giver', instance.giver)
        # instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.itinerary = validated_data.get('itinerary', instance.itinerary)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.reward_date = validated_data.get('reward_date', instance.reward_date)
        instance.save()
        return instance

#Convert Itinerary model to JSON
class ItinerarySerializer(serializers.ModelSerializer):
    #handle creator field as read only
    creator = serializers.ReadOnlyField(source='creator.id')
    class Meta:
        model = apps.get_model('itineraries.Itinerary')
        fields = '__all__'

class ItineraryDetailSerializer(ItinerarySerializer):
    rewards = RewardSerializer(many=True, read_only=True) #serialize list of rewards related to itinerary

    #Updates an instance of the itinerary
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.audience = validated_data.get('audience', instance.audience)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.travel_date = validated_data.get('travel_date', instance.travel_date)
        instance.location = validated_data.get('location', instance.location)
        instance.itinerary_notes = validated_data.get('itinerary_notes', instance.itinerary_notes)
        instance.image = validated_data.get('image', instance.image)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.save()
        return instance