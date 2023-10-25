from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('processDetails', views.processDetails, name='processDetails'),
    path('properties', views.PropertiesList, name='PropertiesList'),
    path('ask', views.AskData, name='AskData'),
]