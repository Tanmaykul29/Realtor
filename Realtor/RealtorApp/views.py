from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
from django.db import IntegrityError
from django.urls import reverse
from .models import User


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":

        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")


def processDetails(request):
    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        limit = request.POST.get('limit')
        print(f"city name is: {city_name} and limit is: {limit}")

        url = "https://realtor.p.rapidapi.com/locations/v2/auto-complete"
        querystring = {"input": city_name, "limit": limit}
        headers = {
            "X-RapidAPI-Key": "your api",
            "X-RapidAPI-Host": "realtor.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            print(data['autocomplete'])
            print(f"length of data: {len(data['autocomplete'])}")

            return render(request, 'properties.html', {
                "data": data['autocomplete'],
                "city_name": city_name,
                "limit": limit
            })
        else:
            return HttpResponse("Failed to retrieve data from the Realtor API.")
    else:
        return render(request, 'ask.html')

def PropertiesList(request):
    return render(request, 'properties.html')


def AskData(request):
    return render(request, 'ask.html')

