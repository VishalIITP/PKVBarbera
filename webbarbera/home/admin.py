from django.contrib import admin

# Register your models here.
from django.contrib import admin

from home.models import reviewsModel

admin.site.register(reviewsModel)

from home.models import  barberaServices
admin.site.register(barberaServices)
