from django.urls import path
from .views import DrumsList, DrumsDetail

urlpatterns = [
    path('', DrumsList.as_view(), name='drums_list'),
    path('<int:pk>/', DrumsDetail.as_view(), name='drums_detail')
]
