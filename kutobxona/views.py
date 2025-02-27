

from rest_framework.generics import ListAPIView
from .models import (Requirements, Editorial, Archive, Abstract, Literature, Sources)
from .serializers import (RequirementsSerializer, EditorialSerializer, ArchiveSerializer, abstractSerializer,
                          LiteratureSerializer, SourcesSerializer)
from django.db.models import Q, Value
from rest_framework.pagination import PageNumberPagination
import re
from django.db.models.functions import Replace, Coalesce
from django.db.models import F


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


class ArchiveListView(ListAPIView):
    queryset = Archive.objects.all().order_by(F('order').asc(nulls_last=True))
    serializer_class = ArchiveSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Archive.objects.all().order_by(F('order').asc(nulls_last=True))
        search_query = self.request.GET.get('search', '').strip()

        if search_query:
            # 1️⃣ Maxsus belgilarni olib tashlash
            search_query = re.sub(r"[^\w\s'-]", "", search_query)

            # 2️⃣ O'zbekcha maxsus harflarni ikkala variantda ham tekshirish
            original_query = search_query
            transformed_query = search_query.replace("O'", "Oʻ").replace("o'", "oʻ")

            # 3️⃣ To‘liq matn bo‘yicha qidirish (ikkala variant bilan)
            full_text_query = Q(title_uz__icontains=original_query) | Q(title_uz__icontains=transformed_query)

            # 4️⃣ Qidiruv so‘zlarini ajratish
            search_words = search_query.split()
            if not search_words:
                return queryset.filter(full_text_query)

            # 5️⃣ Bazadagi 'year' maydonini bo‘sh joylarsiz qilish (123 -yil -> 123yil)
            queryset = queryset.annotate(
                cleaned_year=Replace(
                    Replace(Coalesce(F("year"), Value("")), Value(" "), Value("")),
                    Value("-"), Value("")
                )
            )

            # 6️⃣ Qidirish shartlarini yaratish
            q_objects = Q()
            title_words = []
            year_words = []

            for word in search_words:
                cleaned_word = word.replace(" ", "").replace("-", "")
                if cleaned_word.isdigit() or "yil" in cleaned_word.lower():
                    year_words.append(cleaned_word)
                else:
                    title_words.append(word)

            if title_words and year_words:
                title_query = Q(title_uz__icontains=" ".join(title_words)) | Q(title_uz__iexact=" ".join(title_words))
                year_query = Q(cleaned_year__icontains="".join(year_words))
                q_objects = title_query & year_query
            elif title_words:
                q_objects = Q(title_uz__icontains=" ".join(title_words)) | Q(title_uz__iexact=" ".join(title_words))
            elif year_words:
                q_objects = Q(cleaned_year__icontains="".join(year_words))

            # 🔥 FULL_TEXT_QUERY ni ham qo‘shamiz
            queryset = queryset.filter(full_text_query | q_objects)

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
