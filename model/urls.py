from django.urls import path
from model import views

urlpatterns = [
    path('get_models', views.get_models),
]