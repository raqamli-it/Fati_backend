
from rest_framework import filters
from .models import Talablar, Arxiv
from .serializers import TalabalarSerializer
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from kutobxona.models import Tahrirchi, Manba, Avtoreferat, ElektronKitob
from .serializers import (TahrirchiSerializer, AvtoreferatSerializer, ElektronKitobSerializer,
                          ManbaSerializer)

from .pagination import ResultsSetPagination
from .serializers import ArxivSerializer


class TalablarListView(ListAPIView):
    queryset = Talablar.objects.all()
    serializer_class = TalabalarSerializer


@api_view(['GET'])
def Talablar_detail(request, pk):
    requirements = get_object_or_404(Talablar, pk=pk)
    serializer = TalabalarSerializer(requirements, context={'request': request})
    return Response(serializer.data)


class TahrirchiListCreateView(ListAPIView):
    queryset = Tahrirchi.objects.all()
    serializer_class = TahrirchiSerializer


@api_view(['GET'])
def tahrirchi_detail_view(request, pk):
    tahrirchi = get_object_or_404(Tahrirchi, pk=pk)
    serializer = TahrirchiSerializer(tahrirchi, context={'request': request})
    return Response(serializer.data)


class AvtoreferatListCreateView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AvtoreferatSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Avtoreferat.objects.all().order_by('order')


@api_view(['GET'])
def avtoreferat_detail_view(request, pk):
    avtoreferat = get_object_or_404(Avtoreferat, pk=pk)
    serializer = AvtoreferatSerializer(avtoreferat, context={'request': request})
    return Response(serializer.data)


class ElektronKitobListCreateView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ElektronKitobSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return ElektronKitob.objects.all().order_by('order')


@api_view(['GET'])
def elektron_kitob_detail_view(request, pk):
    elektron_kitob = get_object_or_404(ElektronKitob, pk=pk)
    serializer = ElektronKitobSerializer(elektron_kitob, context={'request': request})
    return Response(serializer.data)


class ManbaListCreateView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ManbaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Manba.objects.all().order_by('order')


@api_view(['GET'])
def manba_detail_view(request, pk):
    manba = get_object_or_404(Manba, pk=pk)
    serializer = ManbaSerializer(manba, context={'request': request})
    return Response(serializer.data)


class ArxivListCreateView(ListAPIView):
    queryset = Arxiv.objects.all()
    serializer_class = ArxivSerializer

    def get_queryset(self):
        return Arxiv.objects.all().order_by('order')


@api_view(['GET'])
def Arxiv_detail_view(request, pk):
    manba = get_object_or_404(Arxiv, pk=pk)
    serializer = ArxivSerializer(manba, context={'request': request})
    return Response(serializer.data)


