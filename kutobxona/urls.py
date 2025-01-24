
from django.urls import path
from .views import (
    TahririyatListCreateView,
    Tahririyat_detail_view,
    AvtoreferatListCreateView,
    avtoreferat_detail_view,
    Talablar_detail,
    TalablarListView,
    Arxiv_detail_view,
    ArxivListCreateView,
    CategoryKitobListCreateView

)

urlpatterns = [

    path('Category/', CategoryKitobListCreateView.as_view(), name='elektronKitob-list'),

    path('avtoreferat/', AvtoreferatListCreateView.as_view(), name='avtoreferat-list'),
    path('avtoreferat/<int:pk>/', avtoreferat_detail_view, name='avtoreferat-detail'),

    path('Tahririyat/', TahririyatListCreateView.as_view(), name='tahrirchi-list'),
    path('Tahririyat/<int:pk>/', Tahririyat_detail_view, name='tahrirchi-detail'),

    path('talablar/', TalablarListView.as_view(), name='talablar-list'),
    path('talablar/<int:pk>/', Talablar_detail, name='talablar-detail'),

    path('arxiv/', ArxivListCreateView.as_view(), name='arxiv-list'),
    path('arxiv/<int:pk>/', Arxiv_detail_view, name='arxiv-detail'),

]

