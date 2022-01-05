from rest_framework import serializers
from covidAPI.models import Country

class CountrySerializer(serializers.ModelSerializer):

    class Meta:

        model = Country
        fields =[

            'country_name',
            'new_cases',
            'total_cases',
            'total_deaths',
            'total_recovered',
            'new_recovered',
            'active_cases',
        ]
