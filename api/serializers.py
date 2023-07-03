from rest_framework import serializers
from api.models import cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ['username', 'nombre', 'email', 'password']