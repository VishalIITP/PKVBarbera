
from typing import ContextManager
from django.contrib import messages
from django.contrib import auth
from django.db.models.base import ModelState
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse


from home.models import barberaServices, reviewsModel


# Create your views here.


def registerPage(request):
    return render(request, 'register.html')


def loginPage(request):
    return render(request, 'login.html')


def polls(request):
    return HttpResponse("This is for Polls of the website")


def homepage(request):
    return render(request, 'KHome.html')


def bookings(request):
    return render(request, 'bookings.html')



def servicesPage(request):
    allServices = barberaServices.objects.all()
    context = {'services': allServices}
    
    
    return render(request, 'servicesPage.html',context)

def contactUsPage(request):
    return render(request, 'contactUs.html')


def tipsPage(request):
    return render(request, 'tipsPage.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')



def faqsPage(request):
    return render(request, 'faq.html')



def myCart(request):
    allServices = barberaServices.objects.all()
    context = {'services': allServices}
    return render(request, 'myCart.html', context)


def logedinhomepage(request):

    return render(request, 'logedinhomepage.html', {})


def rate(request):

    if request.method == "POST":
        # Handle the form
        userRater = request.POST['review-username']
        rating = request.POST['review-rating']
        rating2 = request.POST['review-rating2']
        rating3 = request.POST['review-rating3']
        feedback = request.POST['review-feedback']

        ins = reviewsModel(userRater=userRater, rating=rating,
                           rating2=rating2, rating3=rating3, feedback=feedback,)
        ins.save()

        messages.success(
            request, "Thanks for your kind feedback!! ")

        return redirect('homepage')
    return render(request, 'rate.html')


def reviews(request):
    allReviews = reviewsModel.objects.all()
    context = {'allreviews': allReviews}
    return render(request, 'reviews.html', context)


def createNewUser(request):
    contextCreateNew = {'successNewUser': False}
    if request.method == 'POST':
        username = request.POST['uname']
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        userEmail = request.POST['userEmail']
        password = request.POST['pass1']
        confpassword = request.POST['pass2']

        # Check for errrourneous inputs
        #
        if confpassword != password:
            messages.error(request, "confirm password did'n match")

        if len(username) > 10:
            messages.error(request, "Username must be less than 10 characters")
        # Create the user
        myuser = User.objects.create_user(username, userEmail, password)
        myuser.first_name = firstName
        myuser.last_name = lastName
        myuser.save()
        messages.success(request, "User Created Successfully  ")

        contextCreateNew = {'successNewUser': True}

        return render(request, 'KHome.html', contextCreateNew)

    else:
        return HttpResponse('404-Not Found Enter Details to create User contact-Us:7945656234')


def handlelogin(request):
    if request.method == "POST":
        loginUserName = request.POST['loginUser']
        loginPassword = request.POST['loginPassw']
        print("le to raha hoon")

        barberaUser = authenticate(
            username=loginUserName, password=loginPassword)
            

        if barberaUser is not None:
            login(request, barberaUser)
            messages.success(request, "Successfully Logged In ")
            print("ho raha hoon login")

            return redirect('homepage')

        else:
            messages.error(request, "Invalid Credentials, Please try again")
            print("nahi ho raha hoon login")
            return redirect('homepage')
            

            

    return HttpResponse('404-Not Found')


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully loged out")
    return redirect('homepage')
