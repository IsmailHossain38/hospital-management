from rest_framework import serializers
from . import models

class ContectUsSerializers(serializers.ModelSerializer):
     class Meta:
         model = models.ContectUs
         fields ='__all__'