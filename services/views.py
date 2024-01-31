from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class ServicesUsViewset(viewsets.ModelViewSet):
    queryset =models.Services.objects.all()
    serializer_class = serializers.ServicesSerializers