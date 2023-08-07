from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Itinerary
from .serializers import ItinerarySerializer


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
        return Response(serializer.data) #respond with JSON detailing what was saved