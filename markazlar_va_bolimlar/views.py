
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .models import Xodimlar, Markazlar_Bolimlar, Tadqiqot, Photo, Video
from .serializers import (XodimlarSerializer, MarkazlarBolimlarSerializer, Tadqiqot_Serializer, PhotoSerializer,
                          VideoSerializer, Markazlar_BolimlarSerializer)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class XodimlarListView(ListAPIView):
    queryset = Xodimlar.objects.all().order_by('order')
    serializer_class = XodimlarSerializer


@api_view(['GET'])
def XodimlarDetail(request, pk):
    xodimlar = get_object_or_404(Xodimlar, pk=pk)
    serializer = XodimlarSerializer(xodimlar, context={'request': request})
    return Response(serializer.data)


class MarkazlarBolimlarListCreate(ListAPIView):
    queryset = Markazlar_Bolimlar.objects.all().order_by('order')
    serializer_class = MarkazlarBolimlarSerializer


@api_view(['GET'])
def MarkazlarBolimlarDetail(request, pk):
    markazlarbolimlar = get_object_or_404(Markazlar_Bolimlar, pk=pk)
    serializer = MarkazlarBolimlarSerializer(markazlarbolimlar, context={'request': request})
    return Response(serializer.data)


class TadqiqotListCreate(ListAPIView):
    queryset = Tadqiqot.objects.all().order_by('order')
    serializer_class = Tadqiqot_Serializer


@api_view(['GET'])
def TadqiqotDetail(request, pk):
    tadqiqot = get_object_or_404(Tadqiqot, pk=pk)
    serializer = Tadqiqot_Serializer(tadqiqot, context={'request': request})
    return Response(serializer.data)


class PhotoListCreate(ListAPIView):
    queryset = Photo.objects.all().order_by('order')
    serializer_class = PhotoSerializer


@api_view(['GET'])
def PhotoDetail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    serializer = PhotoSerializer(photo, context={'request': request})
    return Response(serializer.data)


class VideoListCreate(ListAPIView):
    queryset = Video.objects.all().order_by('order')
    serializer_class = VideoSerializer


@api_view(['GET'])
def VideoDetail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    serializer = VideoSerializer(video, context={'request': request})
    return Response(serializer.data)


class ListCreate(ListAPIView):
    queryset = Markazlar_Bolimlar.objects.all()
    serializer_class = Markazlar_BolimlarSerializer