from rest_framework import serializers
from .models import Object, Attribute, Property


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('Index','Type','Related','Name')
