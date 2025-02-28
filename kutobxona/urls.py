
from django.urls import path
from .views import (

    EditorialListCreateView,
    ArchiveListView,
    RequirementsListCreateView,
    AbstractListCreateView,
    LiteratureListCreateView,
    SourcesListCreateView,
)
urlpatterns = [

    path('tahririyat/', EditorialListCreateView.as_view(), name='tahririyat-list'),
    path('talablar/', RequirementsListCreateView.as_view(), name='talablar-list'),
    path('arxivlar/', ArchiveListView.as_view(), name='arxiv-list'),
    path('avtoreferat/', AbstractListCreateView.as_view(), name='tahrirchi-list'),
    path('manbalar/', SourcesListCreateView.as_view(), name='manbalar-list'),
    path('adabiyotlar/', LiteratureListCreateView.as_view(), name='adabiyot-list'),
]