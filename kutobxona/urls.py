
from django.urls import path
from .views import (
    RequirementsListView,
    EditorialListCreateView,
    ArchiveListCreateView,
    Archive_documentListCreateView,
    AbstractListCreateView,
    MatbuotListView,
    FilteredBooksListView,
    PeriodListCreateView,
    FilteredPressListView, FilteredArchiveDocumentsListView,
    Commentcreate
)
urlpatterns = [

    path('tahririyat/', EditorialListCreateView.as_view(), name='tahririyat-list'),
    path('talablar/', RequirementsListView.as_view(), name='talablar-list'),
    path('arxivlar/', ArchiveListCreateView.as_view(), name='arxiv-list'),
    path('avtoreferat/', AbstractListCreateView.as_view(), name='tahrirchi-list'),

    path('books/list', PeriodListCreateView.as_view(), name='period-list'),
    path('books/filter/', FilteredBooksListView.as_view(), name='periods-filter'),
    path('Comment/', Commentcreate.as_view(), name='Comment-post'),

    path('archive_documents/list/', Archive_documentListCreateView.as_view(), name='archive-list'),
    path('archive_documents/filter/', FilteredArchiveDocumentsListView.as_view(), name='filtered-archive_documents'),

    path('matbuot/list/', MatbuotListView.as_view(), name='matbuot-list'),
    path('matbuot/filter/', FilteredPressListView.as_view(), name='matbuot-filter'),
]