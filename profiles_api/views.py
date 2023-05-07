from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloAPIView(APIView):
    """Test API View"""
    sterializers_class = serializers.HelloSeralizer

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
        sterializer = self.sterializers_class(data = request.data)

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