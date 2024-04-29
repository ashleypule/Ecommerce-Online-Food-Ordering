import random
from django.shortcuts import render,redirect

from .models import Product, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django import forms
from django.db.models import Q
import json
from cart.cart import Cart
from . import views
from .models import Locations, driver
from django.views import View
# Create your views here.

def search(request):

     if request.user.is_authenticated:

        if request.method == 'POST':

           searched = request.POST['searched']

           #Query for the product

           searched = Product.objects.filter(Q(name__icontains= searched)) 


           #test for null 

           if not searched:

                messages.success(request, "Product not Found...Please try to search again")


                return render(request, "search.html", {})
           else:

             return render(request, "search.html", {'searched':searched})
        else:

            return render(request, "search.html", {})
        
     else:
         
         return redirect('home')
         


def update_info(request ):

    if request.user.is_authenticated:

        current_user = Profile.objects.get(user__id=request.user.id)
       

       
       
       

        #get original user's Shipping Infor
        form = UserInfoForm (request.POST or None, instance=current_user)


       
       
        if form.is_valid():

            form.save()

            messages.success(request, "Your information has been updated")

            return redirect('home')
        
        return render(request, "update_info.html", {'form':form,})
    else:

         messages.success(request, "login before accessing the page")

         return redirect('home')

def update_password(request):
     
     if request.user.is_authenticated:
         current_user = request.user

         if request.method == 'POST':
             
             form = ChangePasswordForm(current_user, request.POST)

             if form.is_valid():
                 
                 form.save()

                 messages.success(request, "Your password has been updated")

                 login(request, current_user)

                 return redirect('update_user')
             else:
                 
                 for error in list(form.errors.values()):
                     
                     messages.error(request, error)


                     return redirect('update_password')


             
         else:
             
             form = ChangePasswordForm(current_user)
             
             return render(request, "update_password.html", {'form':form})
     else:
          messages.success(request, "You must loggin to view that page ")

     return redirect('update_password')

def update_user(request):

    if request.user.is_authenticated:

        current_user = User.objects.get(id=request.user.id)

        user_form = UpdateUserForm (request.POST or None, instance= current_user)

        if user_form.is_valid():

            user_form.save()

            login(request, current_user)

            messages.success(request, "User has been updated")

            return redirect('home')
        
        return render(request, "update_user.html", {'user_form':user_form})
    else:

         messages.success(request, "login before accessing the page")

         return redirect('home')



def  product(request,pk):

    product = Product.objects.get(id=pk)

    return render(request, 'product.html', {'product':product})


def home(request):

    products = Product.objects.all()

    return render(request, 'home.html', {'products':products})

def menu(request):

    products = Product.objects.all()

    return render(request, 'menu.html', {'products':products})


def about(request):

    return render(request, 'about.html', {})


def login_user(request):

    if request.method == "POST":

        username= request.POST['username']
        password= request.POST['password']
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #Do shopping cart stuff

            current_user = Profile.objects.get(user__id=request.user.id)
            #get their save cart from database

            saved_cart = current_user.old_cart
            #Convert database string to python dictionary

            if  saved_cart:
                #Convert to dictionary us Json

                converted_cart = json.loads(saved_cart)

                cart = Cart(request)

                for key,value in  converted_cart.items():

                    cart.db_add(product=key, quantity=value)











            messages.success(request,("you have been logged In!"))
            return redirect('menu')
        else:

            messages.success(request,("there was erro!"))
            return redirect('login')


            
    else:
 
        return render(request, 'login.html', {})

def logout_user(request):

    logout(request)

    messages.success(request, ("you have been logged out...Thanks"))

    return redirect('home')

def register_user(request):
     
    form = SignUpForm()

    if request.method == "POST":

        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)

            login(request, user)

            messages.success(request, ("Username Created please fill out persona infor....."))

            return redirect('update_info')
        else:

            messages.success(request, ("The was erro please try againg"))


            return redirect('register')
    else:
    
        return render(request, 'register.html', {'form':form})
    





class MapView(View): 
    template_name = "core/map.html"

    def get(self, request):
        key = 'AIzaSyC3Zcg-Rod-bnXvODcqRry4g7Soz5AdjDU'
        eligible_locations = Locations.objects.filter(place_id__isnull=False)
        locations = []

        for location in eligible_locations:
            data = {
                'lat': float(location.lat),
                'lng': float(location.lng),
                'name': location.name
            }
            locations.append(data)

        # Select one random driver
        drivers = list(driver.objects.all())
        selected_driver = None
        if drivers:
            selected_driver = random.choice(drivers)

        context = {
            "key": key,
            "locations": locations,
            "selected_driver": selected_driver,
        }
        return render(request, 'map.html', context)


