from kengashlar.models import Ilmiy_kengash_majlis, fon_picture, Yosh_olimlar
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from kengashlar.serializers import fon_pictureSerializer, Ilmiy_kengash_majlisSerializer, Yosh_olimlarSerializer
from kengashlar.pagination import ResultsSetPagination
from kengashlar.models import Azolar
from kengashlar.serializers import AzolarSerializer
from rest_framework import generics


class fon_pictureListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = fon_pictureSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return fon_picture.objects.all().order_by('order')


@api_view(['GET'])
def fon_picturedetail(request, pk):
    fon_pictur = get_object_or_404(fon_picture, pk=pk)
    serializer = fon_pictureSerializer(fon_pictur, context={'request': request})
    return Response(serializer.data)


class Ilmiy_kengash_majlisListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Ilmiy_kengash_majlisSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Ilmiy_kengash_majlis.objects.all().order_by('order')


#
@api_view(['GET'])
def ilmiy_kengash_majlisdetail(request, pk):
    ilmiy_kengash_majlis = get_object_or_404(Ilmiy_kengash_majlis, pk=pk)
    serializer = Ilmiy_kengash_majlisSerializer(ilmiy_kengash_majlis, context={'request': request})
    return Response(serializer.data)


class Yosh_olimlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Yosh_olimlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Yosh_olimlar.objects.all().order_by('order')


@api_view(['GET'])
def yosh_olimlardetail(request, pk):
    yosh_olimlar = get_object_or_404(Yosh_olimlar, pk=pk)
    serializer = Yosh_olimlarSerializer(yosh_olimlar, context={'request': request})
    return Response(serializer.data)


class AzolarListView(generics.ListAPIView):
    queryset = Azolar.objects.all()
    serializer_class = AzolarSerializer


@api_view(['GET'])
def Azolardetail(request, pk):
    azolar = get_object_or_404(Azolar, pk=pk)
    serializer = AzolarSerializer(azolar, context={'request': request})
    return Response(serializer.data)

#
# class DissertatsiyaIshlarListView(ListAPIView):
#     queryset = DissertatsiyaIshlar.objects.all()
#     serializer_class = DissertatsiyaIshlarSerializer
#
#
# @api_view(['GET'])
# def DissertatsiyaIshlardetail(request, pk):
#     azolar = get_object_or_404(DissertatsiyaIshlar, pk=pk)
#     serializer = DissertatsiyaIshlarSerializer(azolar, context={'request': request})
#     return Response(serializer.data)

# class ContentListView(ListAPIView):
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer
#
#
# @api_view(['GET'])
# def Contentdetail(request, pk):
#     content = get_object_or_404(Content, pk=pk)
#     serializer = ContentSerializer(content, context={'request': request})
#     return Response(serializer.data)
#
