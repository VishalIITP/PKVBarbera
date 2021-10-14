from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage', views.homepage, name='homepage'),
    path('bookings', views.bookings, name='bookings'),
    path('myCart', views.myCart, name='myCart'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('servicesPage', views.servicesPage, name='servicesPage'),
    path('tipsPage', views.tipsPage, name='tipsPage'),
    path('contactUsPage', views.contactUsPage, name='contactUsPage'),
    path('faqsPage', views.faqsPage, name='faqsPage'),

    path('register', views.registerPage, name='registration'),
    path('login', views.loginPage, name='login'),
    path('logedinhomepage', views.logedinhomepage, name="logedinhomepage"),
    path('rate', views.rate, name='rate'),
    path('reviews', views.reviews, name='reviews'),
    path('creatNewUser', views.createNewUser, name='register'),
    path('handlelogin', views.handlelogin, name="handlelogin"),
    path('handlelogout',views.handlelogout,name='handlelogout')
]
