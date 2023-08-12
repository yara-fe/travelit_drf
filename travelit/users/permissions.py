from rest_framework import permissions

#defining a permission class to check if user has permission to access a model
class IsUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj): 

        print("has_object_permission method is being called.")     

        if request.method in permissions.SAFE_METHODS:
            return True
        
        print("Request User:", request.user)
        print("Object User:", obj)
        print("Is Superuser:", request.user.is_superuser)

        # Check if the user is the owner or a superuser/admin
        return obj == request.user or request.user.is_superuser