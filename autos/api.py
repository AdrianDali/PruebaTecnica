from .models import Auto, Marca
from rest_framework import viewsets, permissions
from .serializers import AutoSerializer, MarcaSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AutoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MarcaSerializer