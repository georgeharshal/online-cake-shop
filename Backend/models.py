from django.db import models

# Create your models here.
class categorydb(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    CategoryDescription = models.CharField(max_length=500, null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="Category Image", null=True, blank=True)

class itemsdb(models.Model):
    ItemCategory = models.CharField(max_length=100, null=True, blank=True)
    ItemName = models.CharField(max_length=100, null=True, blank=True)
    ItemPrice = models.IntegerField(null=True, blank=True)
    Image1 = models.ImageField(upload_to="Item Images", null=True, blank=True)
    Image2 = models.ImageField(upload_to="Item Images", null=True, blank=True)
    ItemDescription = models.CharField(max_length=100, null=True, blank=True)
