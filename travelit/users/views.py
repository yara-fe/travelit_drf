from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserList(APIView):

    #GET request for all users
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    #POST request to create a user
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #save a new record
            return Response(
                serializer.data, #respond with JSON detailing what was saved
                status=status.HTTP_201_CREATED #return "Created" when new user is saved
            )
        #return error if serialized data is not valid
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

#Handles specific user information
class CustomUserDetail(APIView):

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404 #return "Not Found" if pk does not exist
        
    #GET request for CustomUser with specific pk
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)