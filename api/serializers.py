from rest_framework import serializers
from api.models import cliente

class ClienteSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField()

    class Meta:
        model = cliente
        fields = ['username', 'nombre', 'email', 'password']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})