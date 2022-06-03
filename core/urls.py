from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('contato', contato),
    path('sobre', sobre),
]
