from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Itinerary, Reward
from .serializers import ItinerarySerializer, RewardSerializer, ItineraryDetailSerializer
from django.http import Http404
from rest_framework import status


class ItineraryList(APIView):

    #GET request for all itineraries
    def get(self, request):
        itineraries = Itinerary.objects.all()
        serializer = ItinerarySerializer(itineraries, many=True)
        return Response(serializer.data)
    
    #POST request to create new itinerary
    def post(self, request):
        serializer = ItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #save a new record
            return Response(
                serializer.data, #respond with JSON detailing what was saved
                status=status.HTTP_201_CREATED #return "Created" when new itinerary is saved
            )
        #return error if serialized data is not valid
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


#Handles specific itinerary
class ItineraryDetail(APIView):

    def get_object(self, pk):
        try:
            return Itinerary.objects.get(pk=pk)
        except Itinerary.DoesNotExist:
            raise Http404 #return "Not Found" if pk does not exist
        
    #GET request for itinerary with specific pk
    def get(self, request, pk):
        itinerary = self.get_object(pk)
        serializer = ItineraryDetailSerializer(itinerary)
        return Response(serializer.data)
    

## REWARD ##
class RewardList(APIView):

    #GET request for all rewards
    def get(self, request):
        rewards = Reward.objects.all()
        serializer = RewardSerializer(rewards, many=True)
        return Response(serializer.data)
    
    #POST request to create new reward
    def post(self, request):
        serializer = RewardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #save a new record
            return Response(
                serializer.data, #respond with JSON detailing what was saved
                status=status.HTTP_201_CREATED #return "Created" when new record is saved
            )
        #return error if serialized data is not valid
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )