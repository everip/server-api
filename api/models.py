from django.db import models
# Create your models here.

class Object(models.Model):
    Index = models.AutoField(primary_key=True)
    Type = models.IntegerField(null=True)
    Related = models.IntegerField(default=-1)
    Name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name

class Attribute(models.Model):
    Index = models.AutoField(primary_key=True)
    Value = models.CharField(max_length=10)

    def __str__(self):
        return self.Value

class Property(models.Model):
    Index = models.AutoField(primary_key=True)
    Object = models.ForeignKey(Object, on_delete=models.CASCADE)
    Attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    def __str__(self):
        return self.Object