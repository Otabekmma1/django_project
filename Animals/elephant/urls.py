from django.urls import path
from .views import index, buy

urlpatterns = [
    path('', index),
    path('buy/', buy),
]
