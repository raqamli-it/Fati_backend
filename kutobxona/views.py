
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import Tahririyat, Avtoreferat, Talablar, Category, Arxiv
from .serializers import (TahririyatSerializer, AvtoreferatSerializer, TalabalarSerializer, CategorySerializer,
                          ArxivSerializer)
from .pagination import ResultsSetPagination


class TalablarListView(ListAPIView):
    queryset = Talablar.objects.all()
    serializer_class = TalabalarSerializer

    def get_queryset(self):
        return Talablar.objects.all().order_by('order')


@api_view(['GET'])
def Talablar_detail(request, pk):
    requirements = get_object_or_404(Talablar, pk=pk)
    serializer = TalabalarSerializer(requirements, context={'request': request})
    return Response(serializer.data)


class TahririyatListCreateView(ListAPIView):
    queryset = Tahririyat.objects.all()
    serializer_class = TahririyatSerializer

    def get_queryset(self):
        return Tahririyat.objects.all().order_by('order')


@api_view(['GET'])
def Tahririyat_detail_view(request, pk):
    tahrirchi = get_object_or_404(Tahririyat, pk=pk)
    serializer = TahririyatSerializer(tahrirchi, context={'request': request})
    return Response(serializer.data)


class AvtoreferatListCreateView(ListAPIView):
    queryset = Avtoreferat.objects.all()
    serializer_class = AvtoreferatSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Avtoreferat.objects.all().order_by('order')


@api_view(['GET'])
def avtoreferat_detail_view(request, pk):
    avtoreferat = get_object_or_404(Avtoreferat, pk=pk)
    serializer = AvtoreferatSerializer(avtoreferat, context={'request': request})
    return Response(serializer.data)


class CategoryKitobListCreateView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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


