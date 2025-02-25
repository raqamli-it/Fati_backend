from django.urls import path
from .views import Institut_tarixiListView, \
    AloqaListView, KaruselListView, \
    RahbariyatListView, Tashkiliy_tuzulmaListView, YangiliklarListView, \
    yangiliklardetail, HavolalarListView, XabarlarCreateView, Kadirlar_bolimiListView

urlpatterns = [
    path('institut-tarixi/', Institut_tarixiListView.as_view(), name='institut_tarixi-list'),
    path('aloqa/', AloqaListView.as_view(), name='aloqa-list'),
    path('xabarlar/', XabarlarCreateView.as_view(), name='xabarlar-create'),
    path('karusel/', KaruselListView.as_view(), name='karusel-list'),
    path('rahbariyat/', RahbariyatListView.as_view(), name='rahbariyat-list'),
    path('tashkiliy-tuzulma/', Tashkiliy_tuzulmaListView.as_view(), name='tashkiliy_tuzulma-list'),\
    path('yangiliklar/', YangiliklarListView.as_view(), name='yangiliklar-list'),
    path('yangiliklar/<int:pk>/', yangiliklardetail, name='yangiliklar-detail'),
    path('havolalar/', HavolalarListView.as_view(), name='havolalar-list'),
    path('kadirlar-bolimi/', Kadirlar_bolimiListView.as_view(), name='kadirlar-bolimi-list'),
]