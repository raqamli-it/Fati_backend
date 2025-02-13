from django.urls import path
from .views import (Xamkor_tashkilotListView, Xamkor_loihalarListView, \
                   Xalqaro_sayohatlarListView, TadqiqotListView, )


urlpatterns = [
    path('xamkor-tashkilot/', Xamkor_tashkilotListView.as_view(), name='xamkor_tashkilot-list'),
    path('xamkor-loihalar/', Xamkor_loihalarListView.as_view(), name='xamkor_loihalar-list'),
    path('xalqaro-sayohatlar/', Xalqaro_sayohatlarListView.as_view(), name='xalqaro_sayohatlar-list'),
    path('tadqiqot/', TadqiqotListView.as_view(), name='tadqiqot-list'),

]
