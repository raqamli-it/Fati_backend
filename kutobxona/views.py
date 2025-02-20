from rest_framework.generics import ListAPIView
from .models import (Requirements, Editorial, Archive, Abstract, Literature, Sources)
from .serializers import (RequirementsSerializer, EditorialSerializer, ArchiveSerializer, abstractSerializer,
                          LiteratureSerializer, SourcesSerializer)

from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


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
        search_query = self.request.GET.get('search', '')

        if search_query:
            search_words = search_query.split()  # So‘zlarni ajratish
            q_objects = Q()

            for word in search_words:
                if word.isdigit():  # Agar faqat son bo‘lsa (masalan: "123")
                    q_objects |= Q(year__icontains=word)
                else:  # Matn bo‘lsa (masalan: "Toshkent")
                    q_objects |= (
                        Q(title__icontains=word) |
                        Q(title_uz__icontains=word) |
                        Q(title_en__icontains=word) |
                        Q(year__icontains=word)
                    )

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


class SourcesSListCreateView(ListAPIView):
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
