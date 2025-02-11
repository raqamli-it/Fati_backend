from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Tahririyat, Avtoreferat, Talablar, Category, Arxiv
from .serializers import (TahririyatSerializer, AvtoreferatSerializer, TalabalarSerializer, CategoryListSerializer,
                          CategoryDetailSerializer, ArxivSerializer)
from rest_framework.pagination import PageNumberPagination


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

    def get_queryset(self):
        return Avtoreferat.objects.all().order_by('order')


@api_view(['GET'])
def avtoreferat_detail_view(request, pk):
    avtoreferat = get_object_or_404(Avtoreferat, pk=pk)
    serializer = AvtoreferatSerializer(avtoreferat, context={'request': request})
    return Response(serializer.data)


class CategoryKitobListCreateView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryKitobDetailView(APIView):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        # 🔍 Search va tilni aniqlash
        search_query = request.query_params.get('search')
        lang = 'title_uz' if request.headers.get('Accept-Language', 'uz').startswith('uz') else 'title_en'

        # 📄 Avtoreferatlar (search bilan)
        avtoreferatlar = category.Avtoreferat.all()
        if search_query:
            avtoreferatlar = avtoreferatlar.filter(**{f"{lang}__icontains": search_query})

        # 📊 Paginatsiya faqat avtoreferatlar uchun
        paginator = ResultsSetPagination()
        avtoreferatlar_page = paginator.paginate_queryset(avtoreferatlar, request)

        # ✅ Category va avtoreferatlar birga qaytariladi
        category_data = CategoryDetailSerializer(category).data
        category_data['avtoreferatlar'] = {
            "count": paginator.page.paginator.count,
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
            "results": AvtoreferatSerializer(avtoreferatlar_page, many=True).data
        }

        return Response(category_data)


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
