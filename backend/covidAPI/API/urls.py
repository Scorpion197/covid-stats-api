from django.urls import path
from .views import *

app_name = "covidAPI"

urlpatterns = [

    path('allcountries/', CountryListView.as_view(), name="get_all_countries"),
]
