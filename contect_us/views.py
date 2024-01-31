from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class ContectUsViewset(viewsets.ModelViewSet):
    queryset =models.ContectUs.objects.all()
    serializer_class = serializers.ContectUsSerializers
