from django.shortcuts import render
from django.http import HttpResponse
from .scraper import Scrapper
# Create your views here.

def test_scrapper(request):

    scrap = Scrapper()
    scrap.extract()
    scrap.process()
    data = scrap.get_results()
    return HttpResponse("hello")
