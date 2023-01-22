from rest_framework import generics
from .models import Drums
from .serializer import DrumsSerializer
from .permissions import IsPurchaserOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class DrumsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Drums.objects.all()
    serializer_class = DrumsSerializer


class DrumsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPurchaserOrReadOnly,)
    queryset = Drums.objects.all()
    serializer_class = DrumsSerializer
