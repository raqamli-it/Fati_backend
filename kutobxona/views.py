from rest_framework.generics import ListAPIView
from .models import (Requirements, Editorial, Archive, Abstract, Literature, Sources, Archive_documents)
from .serializers import (RequirementsSerializer, EditorialSerializer, ArchiveSerializer, abstractSerializer,
                          LiteratureSerializer, SourcesSerializer, Archive_documentsSerializer)

from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class AbstractListCreateView(ListAPIView):
    queryset = Abstract.objects.all().order_by('order')
    serializer_class = abstractSerializer


class EditorialListCreateView(ListAPIView):
    queryset = Editorial.objects.all().order_by('order')
    serializer_class = EditorialSerializer


class ArchiveListCreateView(ListAPIView):
    serializer_class = ArchiveSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Archive.objects.all().order_by('order')
        search_query = self.request.GET.get('search', '')

        if search_query:
            search_words = search_query.split()  # Har bitta so‘zni ajratish
            q_objects = Q()

            for word in search_words:
                if word.isdigit():  # Agar bu faqat son bo‘lsa ("123" kabi)
                    q_objects |= Q(year__icontains=word)
                else:  # Agar bu matn bo‘lsa ("Toshkent" kabi)
                    q_objects |= Q(title__icontains=word) | Q(year__icontains=word)

            queryset = queryset.filter(q_objects)

        return queryset


class RequirementsListCreateView(ListAPIView):
    serializer_class = RequirementsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Requirements.objects.all()
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))

        return queryset


class LiteratureListCreateView(ListAPIView):
    serializer_class = LiteratureSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Literature.objects.all().order_by('order')
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))

        return queryset


class SourcesSListCreateView(ListAPIView):
    serializer_class = SourcesSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Sources.objects.all().order_by('order')
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))

        return queryset


class Archive_documentsListCreateView(ListAPIView):
    serializer_class = Archive_documentsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Archive_documents.objects.all().order_by('order')
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))

        return queryset

