from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .models import Xodimlar, Markazlar, Bolimlar, Tadqiqot, Photo, Video
from .serializers import (XodimlarSerializer, BolimlarSerializer, TadqiqotSerializer, PhotoSerializer,
                          VideoSerializer, MarkazlarSerializer, BolimlarListSerializers, MarkazlarListSerializers)
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
def PhotoDetail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    serializer = PhotoSerializer(photo, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def VideoDetail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    serializer = VideoSerializer(video, context={'request': request})
    return Response(serializer.data)
