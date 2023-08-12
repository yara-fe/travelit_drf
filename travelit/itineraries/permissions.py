from rest_framework import permissions

#defining a permission class to check if user has permission to access a model
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS: 
            return True  #If user is making  a GET request, they have permission
        
        #For other methods, check if user making request is the owner of the object
        if hasattr(obj, 'giver'): #giver is the owner of reward
            return obj.giver == request.user 
        return obj.creator == request.user #creator is the owner of itinerary
        
