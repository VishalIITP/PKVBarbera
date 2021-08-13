# import datetime


from django.db import models
from django.db.models.fields import CharField
# from django.utils import timezone


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self):
#         return self.question_text

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now()-datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text


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
    serviceCategory = models.CharField(max_length=50, default="")
    serviceSubCategory = models.CharField(max_length=50, default="")
    serviceImage = models.ImageField(
        upload_to="home/images", height_field=None, width_field=None, )
    servicePrice = models.CharField(max_length=50, default="0")
    serviceDesc = models.CharField(max_length=300)
    serviceUploadTime = models.DateTimeField()

    def __str__(self):
        return self.serviceName