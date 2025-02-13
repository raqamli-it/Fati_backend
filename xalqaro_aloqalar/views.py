
from rest_framework.generics import ListAPIView
from rest_framework import generics
from .models import Xamkor_tashkilot, Xamkor_loihalar, Xalqaro_sayohatlar, Tadqiqot
from .serializers import (Xamkor_tashkilotSerializer, Xamkor_loihalarSerializer,
                         Ilmiy_safarlarSerializer, TadqiqotSerializer, )


class Xamkor_tashkilotListView(generics.ListAPIView):
    queryset = Xamkor_tashkilot.objects.all().order_by('order')
    serializer_class = Xamkor_tashkilotSerializer


class Xamkor_loihalarListView(generics.ListAPIView):
    queryset = Xamkor_loihalar.objects.all().order_by('order')
    serializer_class = Xamkor_loihalarSerializer


class Xalqaro_sayohatlarListView(generics.ListAPIView):
    queryset = Xalqaro_sayohatlar.objects.all().order_by('order')
    serializer_class = Ilmiy_safarlarSerializer


class TadqiqotListView(ListAPIView):
    queryset = Tadqiqot.objects.all().order_by('order')
    serializer_class = TadqiqotSerializer

