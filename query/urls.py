from django.urls import path
from .views import query

urlpatterns = [
    path('', query, name='query'),
]