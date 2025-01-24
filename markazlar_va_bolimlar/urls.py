from django.urls import path
from .views import (
    XodimlarListView,
    XodimlarDetail,
    MarkazlarBolimlarListCreate,
    MarkazlarBolimlarDetail,
    TadqiqotDetail,
    TadqiqotListCreate,
    PhotoDetail,
    PhotoListCreate,
    VideoDetail,
    VideoListCreate, ListCreate,

)

urlpatterns = [

    path('markazlar_bolimlar/', MarkazlarBolimlarListCreate.as_view(), name='markazlar_bolimlar-list'),
    path('markazlar_bolimlar/<int:pk>/', MarkazlarBolimlarDetail, name='markazlar_bolimlar-detail'),

    path('markazlar_bolimlar_title/', ListCreate.as_view(), name='markazlar_bolimlar-list'),

    path('xodimlar/', XodimlarListView.as_view(), name='xodimlar-list-create'),
    path('xodimlar/<int:pk>/', XodimlarDetail, name='xodimlar-detail'),

    path('tadqiqot/', TadqiqotListCreate.as_view(), name='tadqiqot-list'),
    path('tadqiqot/<int:pk>/', TadqiqotDetail, name='tadqiqot-detail'),

    path('Photo/', PhotoListCreate.as_view(), name='Photo-list'),
    path('Photo/<int:pk>/', PhotoDetail, name='Photo-detail'),

    path('Video/', VideoListCreate.as_view(), name='video-list'),
    path('Video/<int:pk>/', VideoDetail, name='video-detail'),
]
