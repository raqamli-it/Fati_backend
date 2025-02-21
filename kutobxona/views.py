from rest_framework.generics import ListAPIView
from .models import (Requirements, Editorial, Archive, Abstract, Literature, Sources)
from .serializers import (RequirementsSerializer, EditorialSerializer, ArchiveSerializer, abstractSerializer,
                          LiteratureSerializer, SourcesSerializer)

from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
import re


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


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
            # 1️⃣ **Barcha maxsus belgilarni olib tashlash** (`'`, `-`, `.`, `,`, `@`, `#` va h.k.)
            search_query = re.sub(r"[^\w\s]", "", search_query)

            # 2️⃣ **O'zbekcha maxsus harflarni normallashtirish**
            replacements = {
                "O'": "Oʻ", "o'": "oʻ",  # Oʻzbekiston, o‘zbek
                "G'": "Gʻ", "g'": "gʻ",  # Gʻarb, gʻisht
                "Sh": "Sh", "sh": "sh",  # Shahar, shart (bularni almashtirmaslik kerak)
                "Ch": "Ch", "ch": "ch",  # Chiroy, chipta (bularni almashtirmaslik kerak)
            }
            for old, new in replacements.items():
                search_query = search_query.replace(old, new)

            # 3️⃣ **Qidiruv so‘zlarini ajratish va bo‘sh stringlarni oldini olish**
            search_words = [word for word in search_query.split() if word]

            # 4️⃣ **Juda qisqa (1 harfli) so‘zlarni e'tiborga olmaslik**
            if not search_words or all(len(word) < 2 for word in search_words):
                return queryset  # Bo‘sh yoki juda qisqa so‘zlar uchun natija cheklangan

            # 5️⃣ **Qidirish shartlarini yaratish**
            q_objects = Q()
            for word in search_words:
                q_objects |= Q(title_uz__icontains=word)
                q_objects |= Q(title_en__icontains=word)
                q_objects |= Q(year__icontains=word)

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
