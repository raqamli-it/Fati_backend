from .models import Ilmiy_kengash_majlis, Yosh_olimlar
from .serializers import Ilmiy_kengash_majlisSerializer, Yosh_olimlarSerializer
from .models import Azolar, Elonlar
from .serializers import AzolarSerializer, ElonlarSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class Ilmiy_kengash_majlisListView(generics.ListAPIView):
    queryset = Ilmiy_kengash_majlis.objects.all()
    serializer_class = Ilmiy_kengash_majlisSerializer


class Yosh_olimlarListView(generics.ListAPIView):
    queryset = Yosh_olimlar.objects.all()
    serializer_class = Yosh_olimlarSerializer


class AzolarListView(generics.ListAPIView):
    queryset = Azolar.objects.all()
    serializer_class = AzolarSerializer


class ElonlarListView(generics.ListAPIView):
    queryset = Elonlar.objects.all()
    serializer_class = ElonlarSerializer


@api_view(['GET'])
def Elonlardetail(request, pk):
    elonlar = get_object_or_404(Elonlar, pk=pk)
    serializer = ElonlarSerializer(elonlar, context={'request': request})
    return Response(serializer.data)
