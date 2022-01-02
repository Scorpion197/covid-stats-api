from django.db import models

# Create your models here.
class Country(models.Model):

    country_name = models.CharField(max_length=25, default='', null=True, blank=True)
    total_cases = models.CharField(max_length=20, default="", null=True, blank=True)
    new_cases = models.CharField(max_length=20, default="", null=True, blank=True)
    total_deaths = models.CharField(max_length=20, default="", null=True, blank=True)
    new_deaths = models.CharField(max_length=20, default="", null=True, blank=True)
    total_recovered = models.CharField(max_length=20, default="", null=True, blank=True)
    new_recovered = models.CharField(max_length=20, default="", null=True, blank=True)
    active_cases = models.CharField(max_length=20, default="", null=True, blank=True)
    serious_critical = models.CharField(max_length=20, default="", null=True, blank=True)
    population = models.CharField(max_length=20, default="", null=True, blank=True)

    def __str__(self):

        return self.country_name
