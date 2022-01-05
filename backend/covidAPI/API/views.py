from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from .serializers import CountrySerializer
from covidAPI.models import Country


class CountryListView(ListAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class OneCountryListView(ListAPIView):

    serializer_class = CountrySerializer

    def get_queryset(self):

        queryset = Country.objects.all()
        param = self.request.query_params.get('country_name')
        if param is not None:

            queryset = queryset.filter(country_name=param)

        return queryset
