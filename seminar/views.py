from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Seminar_turlari, Seminar
from .serializers import Seminar_turlariSerializer, SeminarSerializer


class Seminar_turlariListView(generics.ListAPIView):
    queryset = Seminar_turlari.objects.all().order_by('order')
    serializer_class = Seminar_turlariSerializer


@api_view(['GET'])
def seminardetail(request, pk):
    seminar = get_object_or_404(Seminar, pk=pk)
    serializer = SeminarSerializer(seminar, context={'request': request})
    return Response(serializer.data)

