from django.urls import path
from intranet import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sistemas', views.sistemas, name='sistemas')
]
