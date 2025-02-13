from .models import Ilmiy_kengash_majlis, Yosh_olimlar
from .serializers import Ilmiy_kengash_majlisSerializer, Yosh_olimlarSerializer
from kengashlar.models import Azolar
from .serializers import AzolarSerializer
from rest_framework import generics


class Ilmiy_kengash_majlisListView(generics.ListAPIView):
    queryset = Ilmiy_kengash_majlis.objects.all()
    serializer_class = Ilmiy_kengash_majlisSerializer


class Yosh_olimlarListView(generics.ListAPIView):
    queryset = Yosh_olimlar.objects.all()
    serializer_class = Yosh_olimlarSerializer


class AzolarListView(generics.ListAPIView):
    queryset = Azolar.objects.all().order_by('order')
    serializer_class = AzolarSerializer
