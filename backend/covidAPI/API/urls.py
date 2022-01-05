from django.urls import path, re_path
from .views import *

app_name = "covidAPI"

urlpatterns = [

    path('allcountries/', CountryListView.as_view(), name="get_all_countries"),
    path('getcountry/', OneCountryListView.as_view(), name="get_one_country"),
]
