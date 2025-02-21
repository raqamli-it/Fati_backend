from rest_framework.generics import ListAPIView
from .models import (Requirements, Editorial, Archive, Abstract, Literature, Sources)
from .serializers import (RequirementsSerializer, EditorialSerializer, ArchiveSerializer, abstractSerializer,
                          LiteratureSerializer, SourcesSerializer)
import re
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.conf import settings


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
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset.order_by('order')
        search_query = self.request.GET.get('search', '').strip()

        if not search_query:
            return queryset

        # Maxsus belgilarni olib tashlash (@, #, -, va boshqalar)
        search_query = re.sub(r'[^\w\s]', '', search_query)
        search_words = search_query.split()

        # PostgreSQL bo'lsa
        if 'postgresql' in settings.DATABASES['default']['ENGINE']:
            search_vector = SearchVector('title', 'title_uz', 'title_en')
            search_query = SearchQuery(search_query)
            queryset = queryset.annotate(search=search_vector).filter(search=search_query)
        else:
            # SQLite va boshqa bazalar uchun optimallashtirish
            q_objects = Q()
            for word in search_words:
                q_objects |= Q(title__icontains=word)
                q_objects |= Q(title_uz__icontains=word)
                q_objects |= Q(title_en__icontains=word)
            queryset = queryset.filter(q_objects)

        return queryset


class ArchiveListCreateView(ListAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset.order_by('order')
        search_query = self.request.GET.get('search', '').strip()

        if not search_query:
            return queryset

        # Maxsus belgilarni olib tashlash
        search_query = re.sub(r'[^\w\s]', '', search_query)
        search_words = search_query.split()

        # PostgreSQL uchun Full-Text Search
        if 'postgresql' in settings.DATABASES['default']['ENGINE']:
            search_vector = SearchVector('title_uz', 'title_en', 'year')
            search_query = SearchQuery(search_query)
            queryset = queryset.annotate(search=search_vector).filter(search=search_query)
        else:
            # SQLite uchun optimallashtirilgan qidiruv
            q_objects = Q()
            for word in search_words:
                q_objects |= Q(title_uz__icontains=word)
                q_objects |= Q(title_en__icontains=word)
                q_objects |= Q(year__icontains=word)
            queryset = queryset.filter(q_objects)

        return queryset


class LiteratureListCreateView(ListAPIView):
    queryset = Literature.objects.all()
    serializer_class = LiteratureSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset.order_by('order')
        search_query = self.request.GET.get('search', '').strip()

        if not search_query:
            return queryset

        # Maxsus belgilarni olib tashlash
        search_query = re.sub(r'[^\w\s]', '', search_query)
        search_words = search_query.split()

        # Agar PostgreSQL bo‘lsa va index qo‘yilmagan bo‘lsa
        if 'postgresql' in settings.DATABASES['default']['ENGINE']:
            search_vector = SearchVector('title', 'title_uz', 'title_en')
            search_query = SearchQuery(search_query)
            queryset = queryset.annotate(search=search_vector).filter(search=search_query)
        else:
            # SQLite uchun optimallashtirilgan qidiruv
            q_objects = Q()
            for word in search_words:
                q_objects |= Q(title__icontains=word)
                q_objects |= Q(title_uz__icontains=word)
                q_objects |= Q(title_en__icontains=word)
            queryset = queryset.filter(q_objects)

        return queryset


class SourcesListCreateView(ListAPIView):
    queryset = Sources.objects.all()
    serializer_class = SourcesSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset.order_by('order')
        search_query = self.request.GET.get('search', '').strip()

        if not search_query:
            return queryset

        # @, #, - va boshqa belgilarni olib tashlash
        search_query = re.sub(r'[^\w\s]', '', search_query)
        search_words = search_query.split()

        # PostgreSQL bo'lsa
        if 'postgresql' in settings.DATABASES['default']['ENGINE']:
            search_vector = SearchVector('title', 'title_uz', 'title_en')
            search_query = SearchQuery(search_query)
            queryset = queryset.annotate(search=search_vector).filter(search=search_query)
        else:
            # SQLite va boshqa bazalar uchun optimallashtirish
            q_objects = Q()
            for word in search_words:
                q_objects |= Q(title__icontains=word)
                q_objects |= Q(title_uz__icontains=word)
                q_objects |= Q(title_en__icontains=word)
            queryset = queryset.filter(q_objects)

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
