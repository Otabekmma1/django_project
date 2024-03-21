from . import views
from django.urls import path

urlpatterns = [
    path('add/<int:x>/<int:y>/', views.qoshish, name='add'),
    path('subtract/<int:x>/<int:y>/', views.ayirish, name='subtract'),
    path('multiply/<int:x>/<int:y>/', views.kopaytirish, name='multiply'),
    path('divide/<int:x>/<int:y>/', views.bolish, name='divide'),
]