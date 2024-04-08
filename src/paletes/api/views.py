from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PaleteSerializer, ColorSerializer
from ..models import Palete, Color


class PaleteListCreateAPIView(ListCreateAPIView):
    serializer_class = PaleteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Palete.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaleteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaleteSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Palete.objects.get(pk=pk, user=self.request.user)


class ColorListCreateAPIView(ListCreateAPIView):
    serializer_class = ColorSerializer

    def get_queryset(self):
        palete_id = self.kwargs.get('palete_id')
        palete = Palete.objects.get(pk=palete_id)
        return Color.objects.filter(palete=palete)

    def perform_create(self, serializer):
        palete_id = self.kwargs.get('palete_id')
        palete = Palete.objects.get(pk=palete_id)
        serializer.save(palete=palete)


class ColorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ColorSerializer

    def get_object(self):
        palete_id = self.kwargs.get('palete_id')
        palete = Palete.objects.get(pk=palete_id)
        pk = self.kwargs.get('pk')
        return Color.objects.get(pk=pk, palete=palete)
