# import datetime


from django.db import models
from django.db.models.fields import CharField

SERVICECATEGORY_CHOICES = (
    ("men", "Men"),
    ("women", "Women"),
    ("wedding", "Wedding"),
    ("kids", "Kids"),


)


# reviews Models

class reviewsModel(models.Model):
    userRater = models.CharField(max_length=30)
    rating = models.IntegerField()
    rating2 = models.IntegerField()
    rating3 = models.IntegerField()
    feedback = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userRater


class barberaServices(models.Model):
    ServiceID = models.AutoField(primary_key=True)
    serviceName = models.CharField(max_length=50, default="")
    serviceImage = models.ImageField(
        upload_to="home/images", height_field=None, width_field=None, )

    serviceCategory = models.CharField(max_length=50,
                                       choices=SERVICECATEGORY_CHOICES,
                                       default="men"
                                       )

   
    serviceCategoryDiscount = models.IntegerField(default="0")

    serviceSubCategory1 = models.CharField(max_length=50, default="Platinum")
    serviceSubCategory1Price = models.IntegerField(default="0")
    serviceSubCategory1Discount = models.IntegerField(default="0")
    serviceSubCategory1Desc = models.CharField(
        max_length=300, default="Barbera Platinum")

    serviceSubCategory2 = models.CharField(max_length=50, default="Gold")
    serviceSubCategory2Price = models.IntegerField(default="0")
    serviceSubCategory2Discount = models.IntegerField(default="0")
    serviceSubCategory2Desc = models.CharField(
        max_length=300, default="Barbera Gold")

    serviceSubCategory3 = models.CharField(max_length=50, default="Silver")
    serviceSubCategory3Price = models.IntegerField(default="0")
    serviceSubCategory3Discount = models.IntegerField(default="0")
    serviceSubCategory3Desc = models.CharField(
        max_length=300, default="Barbera Silver")

    serviceUploadTime = models.DateTimeField()

    def __str__(self):
        return self.serviceName
