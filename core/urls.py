from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('produto/<int:pk>', produto, name='produto'),
]
