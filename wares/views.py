from django.shortcuts import render
from .models import Ware
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import WareSerializer
# Create your views here.
class WareViewSet (viewsets.ModelViewSet):
    queryset=Ware.objects.all()
    serializer_class=WareSerializer
    permission_classes=[permissions.AllowAny]