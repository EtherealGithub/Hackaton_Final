"""
URL configuration for hackatonFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views

records_list = views.ClienteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

records_detail = views.ClienteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', views.My_Home_Login.as_view(), name='My-Home-Login'),
    path('admin/', admin.site.urls),
    path('api/login/', views.ClienteLoginSet.as_view({'post': 'login'}), name='login'),
    path('api/registros/listar', records_list, name='registros-lista'),
    path('api/registros/<int:pk>/', records_detail, name='registros-detalle'),
    path('api/registros/insertar', views.ClienteViewSet.as_view({'post': 'register'}), name='registros-creacion'),
    path('api/consultar/', views.ClienteListView.as_view(), name='cliente-lista'),
]