from .models import Ware
from rest_framework import serializers

class WareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #Which model will get serialized by the class
        model= Ware
        #which fields should be included in the output
        fields = ['id', 'name', 'description', 'category', 'price', 'img']