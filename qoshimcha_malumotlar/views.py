from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Institut_tarixi, Aloqa, Karusel, Rahbariyat, \
    Tashkiliy_tuzulma, Yangiliklar, Havolalar
from .serializers import Institut_tarixiSerializer, \
    AloqaSerializer, KaruselSerializer, RahbariyatSerializer, Tashkiliy_tuzulmaSerializer, YangiliklarSerializer, \
    HavolalarSerializer
from .pagination import ResultsSetPagination


class Institut_tarixiListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Institut_tarixiSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Institut_tarixi.objects.all().order_by('order')


@api_view(['GET'])
def institut_tarixidetail(request, pk):
    institut_tarixi = get_object_or_404(Institut_tarixi, pk=pk)
    serializer = Institut_tarixiSerializer(institut_tarixi, context={'request': request})
    return Response(serializer.data)


class AloqaListView(ListAPIView):
    search_fields = ['phone']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AloqaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Aloqa.objects.all().order_by('order')


@api_view(['GET'])
def aloqadetail(request, pk):
    aloqa = get_object_or_404(Aloqa, pk=pk)
    serializer = AloqaSerializer(aloqa, context={'request': request})
    return Response(serializer.data)


class KaruselListView(ListAPIView):
    queryset = Karusel.objects.all()
    serializer_class = KaruselSerializer


@api_view(['GET'])
def karuseldetail(request, pk):
    karusel = get_object_or_404(Karusel, pk=pk)
    serializer = KaruselSerializer(karusel, context={'request': request})
    return Response(serializer.data)


class RahbariyatListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = RahbariyatSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Rahbariyat.objects.all().order_by('order')


@api_view(['GET'])
def rahbariyatdetail(request, pk):
    rahbariyat = get_object_or_404(Rahbariyat, pk=pk)
    serializer = RahbariyatSerializer(rahbariyat, context={'request': request})
    return Response(serializer.data)


class Tashkiliy_tuzulmaListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Tashkiliy_tuzulmaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Tashkiliy_tuzulma.objects.all().order_by('order')


@api_view(['GET'])
def tashkiliy_tuzulmadetail(request, pk):
    tashkiliy_tuzulma = get_object_or_404(Tashkiliy_tuzulma, pk=pk)
    serializer = Tashkiliy_tuzulmaSerializer(tashkiliy_tuzulma, context={'request': request})
    return Response(serializer.data)


class YangiliklarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = YangiliklarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Yangiliklar.objects.all().order_by('order')


class YangiliklarList(ListAPIView):
    queryset = Yangiliklar.objects.all().order_by('-created_at')[:6]
    serializer_class = YangiliklarSerializer


@api_view(['GET'])
def yangiliklardetail(request, pk):
    yangiliklar = get_object_or_404(Yangiliklar, pk=pk)
    serializer = YangiliklarSerializer(yangiliklar, context={'request': request})
    return Response(serializer.data)


class HavolalarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = HavolalarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Havolalar.objects.all().order_by('order')


@api_view(['GET'])
def havolalardetail(request, pk):
    havolalar = get_object_or_404(Havolalar, pk=pk)
    serializer = HavolalarSerializer(havolalar, context={'request': request})
    return Response(serializer.data)

