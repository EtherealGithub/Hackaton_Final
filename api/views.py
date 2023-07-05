from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from api.models import cliente
from api.serializers import ClienteSerializer

#Vista Principal
from django.http import HttpResponse
from django.views import View
import json

class My_Home_Login(View):
    def get(self, request):
        data = {
            'mensaje': 'Esta es la ventana principal.'
        }
        json_data = json.dumps(data, ensure_ascii=False)

        response = HttpResponse(json_data, content_type='application/json; charset=utf-8')
        return response



from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import LoginSerializer
from .models import cliente

class ClienteLoginSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = LoginSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # Verificar si la combinación de usuario y contraseña existe en la base de datos
        user = cliente.objects.filter(username=username, password=password).first()

        if user:
            return Response({'message': 'Autenticación exitosa.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)
        
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

from rest_framework import viewsets, status
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

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# #Cliente listView opcion 1
from django.http import JsonResponse
from rest_framework import generics
from api.models import cliente
from api.serializers import ClienteSerializer

class ClienteListView(generics.ListAPIView):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

# ##Cliente listView opcion 2

# from rest_framework.response import Response
# from rest_framework.views import APIView
# import json

# class ClienteListView(APIView):
#     def get(self, request, format=None):
#         queryset = cliente.objects.all()
#         serializer = ClienteSerializer(queryset, many=True)
#         data = serializer.data
#         json_data = json.dumps(data, ensure_ascii=False)

#         # Decodificar la cadena JSON para obtener un objeto Python
#         decoded_data = json.loads(json_data)

#         return Response(decoded_data, content_type='application/json; charset=utf-8')

    

    