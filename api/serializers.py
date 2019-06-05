# api/serializers.py
from rest_framework import serializers
from .models import Object, Attribute, Property


class AttributeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attribute
        fields = ('Index', 'Value')


class PropertySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ('Index', 'Object', 'Attribute')


class ObjectSerializers(serializers.HyperlinkedModelSerializer):
    attribute = AttributeSerializers(many=True)

    class Meta:
        model = Object
        fields = ('Index', 'Type', 'Related', 'Name', 'attribute')
