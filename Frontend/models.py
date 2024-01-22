from django.db import models

# Create your models here.
class contactUsdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email_Id = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=300, null=True, blank=True)

class userdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    EmailID = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    ProfileImage = models.ImageField(upload_to="User Profile Images", null=True, blank=True)


class cartdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)



class checkoutdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    ZipCode = models.IntegerField(null=True, blank=True)
    MobileNo = models.IntegerField(null=True, blank=True)
    OrderNotes = models.CharField(max_length=300, null=True, blank=True)