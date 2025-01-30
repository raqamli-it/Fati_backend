from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from xalqaro_aloqalar.models import Xamkor_tashkilot, Xamkor_loihalar, Xalqaro_sayohatlar, Tadqiqot
from xalqaro_aloqalar.pagination import ResultsSetPagination
from xalqaro_aloqalar.serializers import (Xamkor_tashkilotSerializer, Xamkor_loihalarSerializer,
     Xalqaro_sayohatlarSerializer, TadqiqotSerializer,)


class Xamkor_tashkilotListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Xamkor_tashkilotSerializer

    def get_queryset(self):
        return Xamkor_tashkilot.objects.all().order_by('order')


@api_view(['GET'])
def xamkor_tashkilotdetail(request, pk):
    xamkor_tashkilot = get_object_or_404(Xamkor_tashkilot, pk=pk)
    serializer = Xamkor_tashkilotSerializer(xamkor_tashkilot, context={'request': request})
    return Response(serializer.data)


class Xamkor_loihalarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Xamkor_loihalarSerializer

    def get_queryset(self):
        return Xamkor_loihalar.objects.all().order_by('id')

@api_view(['GET'])
def xamkor_loihalardetail(request, pk):
    xamkor_loihalar = get_object_or_404(Xamkor_loihalar, pk=pk)
    serializer = Xamkor_loihalarSerializer(xamkor_loihalar, context={'request': request})
    return Response(serializer.data)


class Xalqaro_sayohatlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Xalqaro_sayohatlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Xalqaro_sayohatlar.objects.all().order_by('order')


@api_view(['GET'])
def xalqaro_sayohatlardetail(request, pk):
    xalqaro_sayohatlar = get_object_or_404(Xalqaro_sayohatlar, pk=pk)
    serializer = Xalqaro_sayohatlarSerializer(xalqaro_sayohatlar, context={'request': request})
    return Response(serializer.data)


class TadqiqotListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = TadqiqotSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Tadqiqot.objects.all().order_by('order')


@api_view(['GET'])
def Tadqiqotdetail(request, pk):
    tadqiqot = get_object_or_404(Tadqiqot, pk=pk)
    serializer = TadqiqotSerializer(tadqiqot, context={'request': request})
    return Response(serializer.data)




