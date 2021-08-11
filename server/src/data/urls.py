from django.urls import path
from .views import accept_data


urlpatterns = [
    path('', accept_data, name='index'),
]