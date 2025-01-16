
from django.urls import path
from .views import (
    TahrirchiListCreateView,
    tahrirchi_detail_view,
    AvtoreferatListCreateView,
    avtoreferat_detail_view,
    ElektronKitobListCreateView,
    elektron_kitob_detail_view,
    ManbaListCreateView,
    manba_detail_view,
    Talablar_detail,
    TalablarListView

)
from .views import Arxiv_detail_view, ArxivListCreateView

from django.urls import path
from .views import TahrirchiListCreateView


urlpatterns = [

    path('tahrirchilar/', TahrirchiListCreateView.as_view(), name='tahrirchi-list'),
    path('tahrirchilar/<int:pk>/', tahrirchi_detail_view, name='tahrirchi-detail'),

    path('avtoreferat/', AvtoreferatListCreateView.as_view(), name='avtoreferat-list'),
    path('avtoreferat/<int:pk>/', avtoreferat_detail_view, name='avtoreferat-detail'),

    path('elektronKitob/', ElektronKitobListCreateView.as_view(), name='elektronKitob-list'),
    path('elektronKitob/<int:pk>/', elektron_kitob_detail_view, name='elektronKitob-detail'),

    path('manbalar/', ManbaListCreateView.as_view(), name='manbalar-list'),
    path('manbalar/<int:pk>/', manba_detail_view, name='manbalar-detail'),

    path('talablar/', TalablarListView.as_view(), name='talablar-list'),
    path('talablar/<int:pk>/', Talablar_detail, name='talablar-detail'),

    path('arxiv/', ArxivListCreateView.as_view(), name='arxiv-list'),
    path('arxiv/<int:pk>/', Arxiv_detail_view, name='arxiv-detail'),

]

