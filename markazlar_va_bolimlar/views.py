from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .models import Xodimlar, Markazlar, Bolimlar, Audio, Rasm, Video
from .serializers import (XodimlarSerializer, BolimlarSerializer, MarkazlarSerializer, BolimlarListSerializers,
                          MarkazlarListSerializers, AudioSerializer, RasmSerializer, VideoSerializer)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class BolimlarList(ListAPIView):
    queryset = Bolimlar.objects.all().order_by('order')
    serializer_class = BolimlarListSerializers


class MarkazlarList(ListAPIView):
    queryset = Markazlar.objects.all().order_by('order')
    serializer_class = MarkazlarListSerializers


@api_view(['GET'])
def BolimlarDetail(request, pk):
    bolimlar = get_object_or_404(Bolimlar, pk=pk)
    serializer = BolimlarSerializer(bolimlar, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def MarkazlarDetail(request, pk):
    markazlar = get_object_or_404(Markazlar, pk=pk)
    serializer = MarkazlarSerializer(markazlar, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def XodimlarDetail(request, pk):
    xodim = get_object_or_404(Xodimlar, pk=pk)
    serializer = XodimlarSerializer(xodim, context={'request': request})
    return Response(serializer.data)


class AudioCreateListAPIView(ListAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


class RasmCreateListAPIView(ListAPIView):
    queryset = Rasm.objects.all()
    serializer_class = RasmSerializer


class VideoCreateListAPIView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
