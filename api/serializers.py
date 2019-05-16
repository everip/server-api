# api/serializers.py
from rest_framework import serializers
from .models import Object, Attribute, Property

class ObjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('Name')

class PropertySerializers(serializers.ModelSerializer):
    Name = ObjectSerializer(many=True, read_only=True)
    class Meta:
        model = Property
        fields = ('ObjectName')

class AttributeSerializers(serializers.ModelSerializer):
    ObjectName = PropertySerializers(many=True, read_only=True)
    class Meta:
        model = Attribute
        fields = ('ObjectName','value')