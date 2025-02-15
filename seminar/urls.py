from django.urls import path

from .views import Seminar_turlariListView,  SeminarListView

urlpatterns = [
    path('seminar-turlari/', Seminar_turlariListView.as_view(), name='seminar_turlari-list'),
    path('seminar/', SeminarListView.as_view(), name='seminar-list'),
]