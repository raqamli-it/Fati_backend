
from rest_framework import generics
from .models import Seminar_turlari, Seminar
from .serializers import Seminar_turlariSerializer, SeminarSerializer


class Seminar_turlariListView(generics.ListAPIView):
    queryset = Seminar_turlari.objects.all().order_by('order')
    serializer_class = Seminar_turlariSerializer


class SeminarListView(generics.ListAPIView):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer
