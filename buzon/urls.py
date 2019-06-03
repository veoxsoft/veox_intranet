from django.urls import path

from buzon import views
from buzon.api.buzon_api import BuzonApi

urlpatterns = [
    path('api/buzon', BuzonApi.as_view()),
    path('', views.index, name='bz_index'),
]