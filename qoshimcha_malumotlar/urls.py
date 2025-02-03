from django.urls import path
from .views import Institut_tarixiListView, institut_tarixidetail, \
    AloqaListView, aloqadetail, KaruselListView, karuseldetail,\
    RahbariyatListView, rahbariyatdetail, Tashkiliy_tuzulmaListView, tashkiliy_tuzulmadetail, YangiliklarListView, \
    yangiliklardetail, HavolalarListView, havolalardetail, YangiliklarList

urlpatterns = [
    path('institut-tarixi/', Institut_tarixiListView.as_view(), name='institut_tarixi-list'),
    path('institut-tarixi/<int:pk>/', institut_tarixidetail, name='institut_tarixi-detail'),

    path('aloqa/', AloqaListView.as_view(), name='aloqa-list'),
    path('aloqa/<int:pk>/', aloqadetail, name='aloqa-detail'),

    path('karusel/', KaruselListView.as_view(), name='karusel-list'),
    path('karusel/<int:pk>/', karuseldetail, name='karusel-detail'),

    path('rahbariyat/', RahbariyatListView.as_view(), name='rahbariyat-list'),
    path('rahbariyat/<int:pk>/', rahbariyatdetail, name='rahbariyat-detail'),

    path('tashkiliy-tuzulma/', Tashkiliy_tuzulmaListView.as_view(), name='tashkiliy_tuzulma-list'),
    path('tashkiliy-tuzulma/<int:pk>/', tashkiliy_tuzulmadetail, name='tashkiliy_tuzulma-detail'),

    path('yangiliklar/', YangiliklarListView.as_view(), name='yangiliklar-list'),
    path('home/yangiliklar/', YangiliklarList.as_view(), name='yangiliklar-home'),
    path('yangiliklar/<int:pk>/', yangiliklardetail, name='yangiliklar-detail'),

    path('havolalar/', HavolalarListView.as_view(), name='havolalar-list'),
    path('havolalar/<int:pk>/', havolalardetail, name='havolalar-detail'),

]