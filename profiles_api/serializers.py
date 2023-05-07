from rest_framework import serializers

class HelloSeralizer(serializers.Serializer):
    """Serializers a name fiwl for testing APIView"""
    name = serializers.CharField(max_length = 10)