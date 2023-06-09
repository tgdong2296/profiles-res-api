from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloAPIView(APIView):
    """Test API View"""
    serializers_class = serializers.HelloSeralizer

    def get(self, request, format = None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Djsngo View',
            'Give you the most control over you application logic',
            'Is maped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        sterializer = self.serializers_class(data = request.data)

        if sterializer.is_valid():
            name = sterializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                sterializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )
        
    def put(self, request, pk = None):
        """Handling updating an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk = None):
        """Handle partical update of an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk = None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializers_class = serializers.HelloSeralizer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial, partial_update)',
            'Automaticaly maps to URLs',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializers_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, request, pk = None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk = None):
        """Handle updating an object by its ID"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk = None):
        """Handle updating part of an object by its ID"""
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk = None):
        """Handle removing an object by its ID"""
        return Response({'http_method': 'DELETE'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating & updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle profile feed item"""
    authentication_classes = (TokenAuthentication,) # Need to authenticate with access token
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all() # Get all objects
    permission_classes = (
        permissions.UpdateOwnStatus,
        #IsAuthenticatedOrReadOnly
        IsAuthenticated
    ) # Config permission

    def perform_create(self, serializer): # Custom creating object by custom function
        """Set user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)