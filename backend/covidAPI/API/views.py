from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from .serializers import CountrySerializer
from ../models import Country


class CountryListView(ListAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    
