
from django.urls import path
from .views import (

    EditorialListCreateView,
    ArchiveListCreateView,
    RequirementsListCreateView,
    AbstractListCreateView,
    LiteratureListCreateView,
    SourcesSListCreateView,
    Archive_documentsListCreateView,
)
urlpatterns = [

    path('tahririyat/', EditorialListCreateView.as_view(), name='tahririyat-list'),
    path('talablar/', RequirementsListCreateView.as_view(), name='talablar-list'),
    path('arxivlar/', ArchiveListCreateView.as_view(), name='arxiv-list'),
    path('avtoreferat/', AbstractListCreateView.as_view(), name='tahrirchi-list'),

    path('manbalar/', SourcesSListCreateView.as_view(), name='manbalar-list'),
    path('adabiyotlar/', LiteratureListCreateView.as_view(), name='adabiyot-list'),
    path('archive_documents/list/', Archive_documentsListCreateView.as_view(), name='archive-list'),
]