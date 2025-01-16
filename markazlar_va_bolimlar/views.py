import objects
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .models import Xodimlar, MarkazlarBolimlar
from .serializers import XodimlarSerializer, MarkazlarBolimlarSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class XodimlarListView(ListAPIView):
    queryset = Xodimlar.objects.all()
    serializer_class = XodimlarSerializer

    def get_queryset(self):
        return Xodimlar.objects.all().order_by('order')


@api_view(['GET'])
def XodimlarDetail(request, pk):
    xodimlar = get_object_or_404(Xodimlar, pk=pk)
    serializer = XodimlarSerializer(xodimlar, context={'request': request})
    return Response(serializer.data)


class MarkazlarBolimlarListCreate(ListAPIView):
    queryset = MarkazlarBolimlar.objects.all()
    serializer_class = MarkazlarBolimlarSerializer

    def get_queryset(self):
        return MarkazlarBolimlar.objects.all().order_by('order')


@api_view(['GET'])
def MarkazlarBolimlarDetail(request, pk):
    markazlarbolimlar = get_object_or_404(MarkazlarBolimlar, pk=pk)
    serializer = MarkazlarBolimlarSerializer(markazlarbolimlar, context={'request': request})
    return Response(serializer.data)
