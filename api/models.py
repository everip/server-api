from django.db import models

# Create your models here.


class Object(models.Model):
    Index = models.AutoField(primary_key=True)
    Type = models.IntegerField(null=True)
    Related = models.ForeignKey('Object', on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=100)
    

class Attribute(models.Model):
    Index = models.AutoField(primary_key=True)
    Value = models.CharField(max_length=10)


class Property(models.Model):
    Index = models.AutoField(primary_key=True)
    Object = models.ForeignKey(Object, on_delete=models.CASCADE)
    Attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
