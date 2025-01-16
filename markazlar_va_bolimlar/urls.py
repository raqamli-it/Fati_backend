from django.urls import path
from .views import (
    XodimlarListView,
    XodimlarDetail,
    MarkazlarBolimlarListCreate,
    MarkazlarBolimlarDetail
)

urlpatterns = [

    path('xodimlar/', XodimlarListView.as_view(), name='xodimlar-list-create'),
    path('xodimlar/<int:pk>/', XodimlarDetail, name='xodimlar-detail'),

    path('markazlar_bolimlar/', MarkazlarBolimlarListCreate.as_view(), name='markazlar-bolimlar-list'),
    path('markazlar_bolimlar/<int:pk>/', MarkazlarBolimlarDetail, name='markkaa-bolimlar-detail'),
]
