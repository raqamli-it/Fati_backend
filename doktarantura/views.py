from rest_framework import generics
from .models import Qabul_tartibi, Malakaviy_imtihon, Doktarantura
from .serializers import Qabul_tartibiSerializer, Malakaviy_imtihonSerializer, DoktaranturaSerializer


class Qabul_tartibiListView(generics.ListAPIView):
    queryset = Qabul_tartibi.objects.all().order_by('order')
    serializer_class = Qabul_tartibiSerializer


class Malakaviy_imtihonListView(generics.ListAPIView):
    queryset = Malakaviy_imtihon.objects.all().order_by('order')
    serializer_class = Malakaviy_imtihonSerializer


class DoktaranturaListView(generics.ListAPIView):
    queryset = Doktarantura.objects.all().order_by('order')
    serializer_class = DoktaranturaSerializer
