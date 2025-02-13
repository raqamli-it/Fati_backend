from django.urls import path

from .views import Qabul_tartibiListView, Malakaviy_imtihonListView, \
    DoktaranturaListView

urlpatterns = [
    path('qabul-tartibi/', Qabul_tartibiListView.as_view()),
    path('malakaviy-imtihon/', Malakaviy_imtihonListView.as_view()),
    path('doktarantura/', DoktaranturaListView.as_view()),
]