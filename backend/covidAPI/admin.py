from django.contrib import admin
from .models import Country
# Register your models here.

class AdminCountry(admin.ModelAdmin):

    list_display = ('country_name', )

admin.site.register(Country, AdminCountry)
