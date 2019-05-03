from django.db import models

# Create your models here.
class Object(models.Model):
    Index = models.AutoField(primary_key=True)
    Type = models.IntegerField(null=True, blank=True)
    Related = models.IntegerField(null=True, blank=True)
    Name = models.CharField(max_length=20)

class Attribute(models.Model):
    Index = models.AutoField(primary_key=True)
    Value = models.CharField(max_length=5)

class Property(models.Model):
    Index = models.AutoField(primary_key=True)
    Object = models.IntegerField(null=True, blank=True)
    Attribute = models.IntegerField(null=True, blank=True)    