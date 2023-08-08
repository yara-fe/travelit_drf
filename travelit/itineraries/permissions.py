from rest_framework import permissions

#defining a permission class to check if user has permission to access a model
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS: 
            return True  #If user is making  a GET request, they have permission
        return obj.creator == request.user #For other methods, check if user making request is saved in creator field