from django.urls import path
from qoshimcha_malumotlar.views import Institut_tarixiListView, institut_tarixidetail, \
    AloqaListView, aloqadetail, KaruselListView, karuseldetail,\
    RahbariyatListView, rahbariyatdetail, Tashkiliy_tuzulmaListView, tashkiliy_tuzulmadetail, YangiliklarListView, \
    yangiliklardetail, HavolalarListView, havolalardetail, pictureListView, picturedetail, Kengash_rasmListView, Kengash_rasmdetail

urlpatterns = [
    path('institut-tarixi/', Institut_tarixiListView.as_view(), name='institut_tarixi-list'),
    path('institut-tarixi/<int:pk>/', institut_tarixidetail, name='institut_tarixi-detail'),


    path('aloqa/', AloqaListView.as_view(), name='aloqa-list'),
    path('aloqa/<int:pk>/', aloqadetail, name='aloqa-detail'),

    path('Kengash_rasm/', Kengash_rasmListView.as_view(), name='kengash_rasm-list'),
    path('Kengash_rasm/<int:pk>/', Kengash_rasmdetail, name='kengash_rasm-detail'),

    path('karusel/', KaruselListView.as_view(), name='karusel-list'),
    path('karusel/<int:pk>/', karuseldetail, name='karusel-detail'),

    path('rahbariyat/', RahbariyatListView.as_view(), name='rahbariyat-list'),
    path('rahbariyat/<int:pk>/', rahbariyatdetail, name='rahbariyat-detail'),

    path('tashkiliy-tuzulma/', Tashkiliy_tuzulmaListView.as_view(), name='tashkiliy_tuzulma-list'),
    path('tashkiliy-tuzulma/<int:pk>/', tashkiliy_tuzulmadetail, name='tashkiliy_tuzulma-detail'),

    path('yangiliklar/', YangiliklarListView.as_view(), name='yangiliklar-list'),
    path('yangiliklar/<int:pk>/', yangiliklardetail, name='yangiliklar-detail'),

    path('havolalar/', HavolalarListView.as_view(), name='havolalar-list'),
    path('havolalar/<int:pk>/', havolalardetail, name='havolalar-detail'),

    path('picture/', pictureListView.as_view(), name='picture_list'),
    path('picture/<int:pk>/', picturedetail, name='picture_detail'),
]