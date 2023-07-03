from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from api.models import cliente
from api.serializers import ClienteSerializer

# class ClienteViewSet(viewsets.ModelViewSet):
#     queryset = cliente.objects.all()
#     serializer_class = ClienteSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = cliente.objects.get(username=username, password=password)
            return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        except cliente.DoesNotExist:
            return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        


        
# from rest_framework.decorators import action
# from rest_framework.response import Response

# class ClienteViewSet(viewsets.ModelViewSet):
#     queryset = cliente.objects.all()
#     serializer_class = ClienteSerializer

#     @action(detail=False, methods=['post'])
#     def register(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
from rest_framework.decorators import action
from rest_framework.response import Response

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        email = request.data.get('email')

        # Verificar si el correo ya existe en la base de datos
        if cliente.objects.filter(email=email).exists():
            return Response({'error': 'El correo ya está registrado.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
