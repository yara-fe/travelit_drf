from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Itinerary, Reward
from .serializers import ItinerarySerializer, RewardSerializer, ItineraryDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly


class ItineraryList(APIView):

    #Everything is Read Only, unless you are logged in
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #GET request for all itineraries
    def get(self, request):
        itineraries = Itinerary.objects.all()
        serializer = ItinerarySerializer(itineraries, many=True)
        return Response(serializer.data)
    
    #POST request to create new itinerary
    def post(self, request):
        serializer = ItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user) #save a new record  and hand user info to creator field
            return Response(
                serializer.data, #respond with JSON detailing what was saved
                status=status.HTTP_201_CREATED #return "Created" when new itinerary is saved
            )
        #return error if serialized data is not valid
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


#Handles specific itinerary information
class ItineraryDetail(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            itinerary = Itinerary.objects.get(pk=pk)
            self.check_object_permissions(self.request, itinerary)
            return itinerary
        except Itinerary.DoesNotExist:
            raise Http404 #return "Not Found" if pk does not exist
        
    #GET request for itinerary with specific pk
    def get(self, request, pk):
        itinerary = self.get_object(pk)
        serializer = ItineraryDetailSerializer(itinerary)
        return Response(serializer.data)
    
    #Replace a record with an updated version
    def put(self, request, pk):
        itinerary = self.get_object(pk)
        serializer = ItineraryDetailSerializer(
            instance=itinerary,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Delete a record
    def delete(self, request, pk):
        itinerary = self.get_object(pk)
        itinerary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


## REWARDS ##

class RewardList(APIView):
     #Everything is Read Only, unless you are logged in
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #GET request for all rewards
    def get(self, request):
        rewards = Reward.objects.all()
        serializer = RewardSerializer(rewards, many=True)
        return Response(serializer.data)
    
    #POST request to create new reward
    def post(self, request):
        serializer = RewardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(giver=request.user) #save a new record
            return Response(
                serializer.data, #respond with JSON detailing what was saved
                status=status.HTTP_201_CREATED #return "Created" when new record is saved
            )
        #return error if serialized data is not valid
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class RewardDetail(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            reward = Reward.objects.get(pk=pk)
            self.check_object_permissions(self.request, reward)
            return reward
        except Reward.DoesNotExist:
            raise Http404 #return "Not Found" if pk does not exist
    
    def get(self,request, pk):
        reward = self.get_object(pk)
        serializer = RewardSerializer(reward)
        return Response(serializer.data)
    
    #Replace a record with an updated version
    def put(self, request, pk):
        reward = self.get_object(pk)
        serializer = RewardSerializer(
            instance=reward,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Delete a reward record
    def delete(self, request, pk):
        reward = self.get_object(pk)
        reward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)