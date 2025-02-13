from django.urls import path

from .views import Seminar_turlariListView,  seminardetail

urlpatterns = [
    path('seminar-turlari/', Seminar_turlariListView.as_view(), name='seminar_turlari-list'),
    path('seminar/<int:pk>/', seminardetail, name='seminar-detail'),
]