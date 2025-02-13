from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status, generics, pagination
from .models import (Requirements, Editorial, Archive, Period, Books, Period_filter,
                     archive_documents, Abstract, Mat_category, Year_filter, Region_filter, the_press, Comment)
from .serializers import (RequirementsSerializer, EditorialSerializer, ArchiveSerializer,
                          PeriodListSerializer, BooksSerializer, Period_filterSerializer, archive_documentsSerializer,
                          abstractSerializer, Mat_categorySerializer, Year_filterSerializer, Region_filterSerializer,
                          the_pressSerializer, CommentSerializer)


class RequirementsListView(ListAPIView):
    queryset = Requirements.objects.all().order_by('order')
    serializer_class = RequirementsSerializer


class EditorialListCreateView(ListAPIView):
    queryset = Editorial.objects.all().order_by('order')
    serializer_class = EditorialSerializer


class ArchiveListCreateView(ListAPIView):
    queryset = Archive.objects.all().order_by('order')
    serializer_class = ArchiveSerializer


class AbstractListCreateView(ListAPIView):
    queryset = Abstract.objects.all().order_by('order')
    serializer_class = abstractSerializer


class PeriodListCreateView(ListAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodListSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10  # Har bir sahifada 10 ta kitob chiqadi
    page_size_query_param = 'page_size'  # Foydalanuvchi sahifa hajmini o‘zgartira oladi
    max_page_size = 50


class FilteredBooksListView(generics.ListAPIView):
    serializer_class = BooksSerializer
    pagination_class = CustomPagination  # Maxsus paginatsiya klassi ishlatiladi

    def get_queryset(self):
        queryset = Books.objects.all().order_by("order")
        period_ids = self.request.GET.getlist('period_id')  # Bir nechta `period_id` olish
        search_query = self.request.GET.get('search', '')  # Kitob nomi bo‘yicha qidiruv

        filters = Q()
        if period_ids:
            filters &= Q(period__id__in=period_ids)  # Period bo‘yicha filter

        if search_query:
            filters &= Q(title__icontains=search_query)  # Kitob nomi bo‘yicha qidiruv

        if filters:
            queryset = queryset.filter(filters).distinct()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "Hech qanday natija topilmadi", "data": []}, status=status.HTTP_200_OK)

        # Paginatsiya qo‘shildi
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = BooksSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = BooksSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Archive_documentListCreateView(ListAPIView):
    queryset = Period_filter.objects.all()
    serializer_class = Period_filterSerializer


class FilteredArchiveDocumentsListView(generics.ListAPIView):
    serializer_class = archive_documentsSerializer
    pagination_class = CustomPagination  # Paginatsiya qo‘shildi

    def get_queryset(self):
        queryset = archive_documents.objects.all().order_by("order")
        period_filter_ids = self.request.GET.getlist('period_filter_id')  # Bir nechta ID olish
        search_query = self.request.GET.get('search', '')  # Qidiruv uchun so‘rov

        filters = Q()  # Dinamik filter

        if period_filter_ids:
            filters &= Q(period_filter__id__in=period_filter_ids)  # ManyToMany uchun filter

        if search_query:
            filters &= Q(title__icontains=search_query)  # Qidiruv funksiyasi

        if filters:
            queryset = queryset.filter(filters).distinct()  # ManyToMany uchun distinct()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "Hech qanday natija topilmadi", "data": []}, status=status.HTTP_200_OK)

        # Paginatsiya
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = archive_documentsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = archive_documentsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MatbuotListView(APIView):
    def get(self, request, *args, **kwargs):
        mat_categories = Mat_category.objects.all()
        years = Year_filter.objects.all()
        regions = Region_filter.objects.all()

        mat_serializer = Mat_categorySerializer(mat_categories, many=True)
        year_serializer = Year_filterSerializer(years, many=True)
        region_serializer = Region_filterSerializer(regions, many=True)

        return Response({
            "mat_categories": mat_serializer.data,
            "years": year_serializer.data,
            "regions": region_serializer.data
        }, status=status.HTTP_200_OK)


class FilteredPressListView(generics.ListAPIView):
    serializer_class = the_pressSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = the_press.objects.all().order_by("order")
        mat_cotegory_ids = self.request.GET.getlist('mat_cotegory_id')
        year_ids = self.request.GET.getlist('year_id')
        region_ids = self.request.GET.getlist('region_id')
        search_query = self.request.GET.get('search', '')

        q_objects = Q()

        if mat_cotegory_ids:
            q_objects |= Q(mat_cotegory_id__in=mat_cotegory_ids)  # OR sharti qo‘llandi
        if year_ids:
            q_objects |= Q(year_id__in=year_ids)
        if region_ids:
            q_objects |= Q(region_id__in=region_ids)
        if search_query:
            q_objects |= Q(title__icontains=search_query)

        if q_objects:
            queryset = queryset.filter(q_objects).distinct().order_by("order")

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "Hech qanday natija topilmadi", "data": []}, status=status.HTTP_200_OK)

        # Paginatsiya
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = the_pressSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = the_pressSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Commentcreate(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
