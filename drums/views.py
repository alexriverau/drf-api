from rest_framework import generics
from .models import Drums
from .serializer import DrumsSerializer


class DrumsList(generics.ListCreateAPIView):
    queryset = Drums.objects.all()
    serializer_class = DrumsSerializer


class DrumsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drums.objects.all()
    serializer_class = DrumsSerializer
