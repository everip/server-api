# api/serializers.py
from rest_framework import serializers
from .models import Object, Attribute, Property
from rest_framework.renderers import JSONRenderer


class AttributeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('Index', 'Value')


class PropertySerializers(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('Index','Object','Attribute')


class ObjectSerializers(serializers.ModelSerializer):
    sub_attribute = PropertySerializers(many=True, read_only=True)

    class Meta:
        model = Object
        fields = ('Index', 'Type', 'Related', 'Name', 'sub_attribute')
