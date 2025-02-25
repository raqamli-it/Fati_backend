

from rest_framework.generics import ListAPIView
from .models import (Requirements, Editorial, Archive, Abstract, Literature, Sources)
from .serializers import (RequirementsSerializer, EditorialSerializer, ArchiveSerializer, abstractSerializer,
                          LiteratureSerializer, SourcesSerializer)
from django.db.models import Q, Value
from rest_framework.pagination import PageNumberPagination
import re


class CustomPagination(PageNumberPagination):
    page_size = 16
    page_size_query_param = 'page_size'
    max_page_size = 1000


class RequirementsListCreateView(ListAPIView):
    queryset = Requirements.objects.all().order_by('order')
    serializer_class = RequirementsSerializer


class AbstractListCreateView(ListAPIView):
    serializer_class = abstractSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Abstract.objects.all().order_by('order')
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(title_uz__icontains=search_query) |
                Q(title_en__icontains=search_query)
            )

        return queryset


class EditorialListCreateView(ListAPIView):
    serializer_class = EditorialSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Editorial.objects.all().order_by('order')
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(title_uz__icontains=search_query) |
                Q(title_en__icontains=search_query)
            )

        return queryset


class ArchiveListCreateView(ListAPIView):
    serializer_class = ArchiveSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Archive.objects.all().order_by('order')
        search_query = self.request.GET.get('search', '').strip()

        if search_query:
            # 1️⃣ **Barcha maxsus belgilarni olib tashlash**
            search_query = re.sub(r"[^\w\s'-]", "", search_query)

            # 2️⃣ **O'zbekcha maxsus harflarni normallashtirish**
            replacements = {
                "O'": "Oʻ", "o'": "oʻ",
                "G'": "Gʻ", "g'": "gʻ"
            }
            for old, new in replacements.items():
                search_query = search_query.replace(old, new)

            # 3️⃣ **Qidiruv so‘zlarini ajratish**
            search_words = [word.strip() for word in search_query.split() if word.strip()]
            if len(search_words) < 2:
                return queryset  # Kamida 2 so‘z bo‘lishi kerak (title va year uchun)

            # 4️⃣ **Bazadagi 'year' maydonini bo‘sh joylarsiz qilish**
            from django.db.models.functions import Replace
            queryset = queryset.annotate(cleaned_year=Replace("year", Value(" "), Value("")))

            # 5️⃣ **Qidiruv shartlarini yaratish**
            q_objects = Q()
            for i in range(len(search_words) - 1):
                q_objects |= (Q(title_uz__icontains=search_words[i]) & Q(cleaned_year__icontains=search_words[i + 1]))

            queryset = queryset.filter(q_objects)

        return queryset

class LiteratureListCreateView(ListAPIView):
    serializer_class = LiteratureSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Literature.objects.all().order_by('order')
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(title_uz__icontains=search_query) |
                Q(title_en__icontains=search_query)
            )

        return queryset


class SourcesListCreateView(ListAPIView):
    serializer_class = SourcesSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Sources.objects.all().order_by('order')
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(title_uz__icontains=search_query) |
                Q(title_en__icontains=search_query)
            )

        return queryset
#
#
# class Archive_documentsListCreateView(ListAPIView):
#     serializer_class = Archive_documentsSerializer
#     pagination_class = CustomPagination
#
#     def get_queryset(self):
#         queryset = Archive_documents.objects.all().order_by('order')
#         search_query = self.request.GET.get('search', '')
#
#         if search_query:
#             queryset = queryset.filter(
#                 Q(title__icontains=search_query) |
#                 Q(title_uz__icontains=search_query) |
#                 Q(title_en__icontains=search_query)
#             )
#
#         return queryset
