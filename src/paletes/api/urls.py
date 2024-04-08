from django.urls import path

from .views import (
    PaleteRetrieveUpdateDestroyAPIView,
    PaleteListCreateAPIView,
    ColorRetrieveUpdateDestroyAPIView,
    ColorListCreateAPIView
)

urlpatterns = [
    path('palete/<int:pk>', PaleteRetrieveUpdateDestroyAPIView.as_view(), name='palete-detail'),
    path('palete/', PaleteListCreateAPIView.as_view(), name='palete-list'),
    path('color/<int:palete_id>/<int:pk>', ColorRetrieveUpdateDestroyAPIView.as_view(), name='color-detail'),
    path('color/<int:palete_id>/', ColorListCreateAPIView.as_view(), name='color-list'),
]
