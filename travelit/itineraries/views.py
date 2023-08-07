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