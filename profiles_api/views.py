from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format = None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Djsngo View',
            'Give you the most control over you application logic',
            'Is maped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})