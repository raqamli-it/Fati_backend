from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Institut_tarixi, Aloqa, Karusel, Rahbariyat, \
    Tashkiliy_tuzulma, Yangiliklar, Havolalar, Xabarlar, Category, Xodimlar_turlari
from .serializers import Institut_tarixiSerializer, \
    AloqaSerializer, KaruselSerializer, RahbariyatSerializer, Tashkiliy_tuzulmaSerializer, YangiliklarSerializer, \
    HavolalarSerializer, XabarlarSerializer, CategorySerializer, Xodimlar_turlariSerializer
from rest_framework.pagination import PageNumberPagination


class Institut_tarixiListView(ListAPIView):
    queryset = Institut_tarixi.objects.all().order_by('order')
    serializer_class = Institut_tarixiSerializer


class AloqaListView(ListAPIView):
    queryset = Aloqa.objects.all()
    serializer_class = AloqaSerializer


class XabarlarCreateView(generics.CreateAPIView):  # Faqat POST uchun
    queryset = Xabarlar.objects.all()
    serializer_class = XabarlarSerializer


class KaruselListView(ListAPIView):
    queryset = Karusel.objects.all()
    serializer_class = KaruselSerializer


class RahbariyatListView(ListAPIView):
    queryset = Rahbariyat.objects.all().order_by('order')
    serializer_class = RahbariyatSerializer


class Tashkiliy_tuzulmaListView(ListAPIView):
    queryset = Tashkiliy_tuzulma.objects.all().order_by('order')
    serializer_class = Tashkiliy_tuzulmaSerializer


class YangiliklarPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000


class YangiliklarListView(ListAPIView):
    queryset = Yangiliklar.objects.all().order_by('-created_at')
    serializer_class = YangiliklarSerializer
    pagination_class = YangiliklarPagination


@api_view(['GET'])
def yangiliklardetail(request, pk):
    yangiliklar = get_object_or_404(Yangiliklar, pk=pk)
    serializer = YangiliklarSerializer(yangiliklar, context={'request': request})
    return Response(serializer.data)


class HavolalarListView(ListAPIView):
    queryset = Havolalar.objects.all().order_by('order')
    serializer_class = HavolalarSerializer


class Kadirlar_bolimiListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Xodimlar_turlariListView(ListAPIView):
    queryset = Xodimlar_turlari.objects.all()
    serializer_class = Xodimlar_turlariSerializer
