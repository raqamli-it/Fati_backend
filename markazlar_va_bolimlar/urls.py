from django.urls import path
from .views import (BolimlarList, BolimlarDetail, MarkazlarList, MarkazlarDetail, XodimlarDetail,
                    AudioCreateListAPIView, RasmCreateListAPIView, VideoCreateListAPIView)


urlpatterns = [
    path('bolimlar-list', BolimlarList.as_view(), name='markazlar_title-list'),
    path('bolim/<int:pk>', BolimlarDetail, name='bolimlar-detail'),

    path('markazlar-list', MarkazlarList.as_view(), name='bolimlar_title-list'),
    path('markaz/<int:pk>', MarkazlarDetail, name='markazlar-detail'),

    path('audio/', AudioCreateListAPIView.as_view(), name='audio-list'),
    path('photo/', RasmCreateListAPIView.as_view(), name='photo-list'),
    path('video/', VideoCreateListAPIView.as_view(), name='video-list'),


    path('Xodimlar/<int:pk>', XodimlarDetail, name='xodimlar-detail'),

]
