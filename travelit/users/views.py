from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsUserOrReadOnly


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

    #Everything is Read Only, unless you are logged in
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsUserOrReadOnly]

    def get_object(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user) #check whether the user making the request has the necessary permissions to access the user object
            return user
        except CustomUser.DoesNotExist:
            raise Http404 #return "Not Found" if pk does not exist
        
    #GET request for CustomUser with specific pk
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    #Replace a user record with an updated version (permission required)
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(
            instance=user,
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
    
    # Delete a user (permission required)
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    