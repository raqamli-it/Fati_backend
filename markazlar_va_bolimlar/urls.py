from django.urls import path
from .views import (BolimlarList, BolimlarDetail, MarkazlarList, MarkazlarDetail,
                    PhotoDetail, VideoDetail, XodimlarDetail)

urlpatterns = [
    path('bolimlar-list', BolimlarList.as_view(), name='markazlar_title-list'),
    path('bolim/<int:pk>', BolimlarDetail, name='bolimlar-detail'),

    path('markazlar-list', MarkazlarList.as_view(), name='bolimlar_title-list'),
    path('markaz/<int:pk>', MarkazlarDetail, name='markazlar-detail'),

    path('Photo/<int:pk>', PhotoDetail, name='Photo-detail'),
    path('Video/<int:pk>', VideoDetail, name='video-detail'),

    path('Xodimlar/<int:pk>', XodimlarDetail, name='xodimlar-detail'),

]
