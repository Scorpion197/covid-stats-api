from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include 
from .views import * 

app_name = 'covidAPI'

urlpatterns = [
    
    path("test/", test_scrapper, name="test"), 
]