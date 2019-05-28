# api/serializers.py
from rest_framework import serializers
from .models import Object, Attribute, Property

class ObjectSerializers(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=True)
    #def continent(): serializers customize
    
        class Meta:
            model = Object
            fields = ('Index','Type','Related','Name','attribute')

class PropertySerializers(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('Index','Object','Attribute')

class AttributeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('Index','Value')