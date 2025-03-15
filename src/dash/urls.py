from django.urls import path
from dash import views

urlpatterns = [
    path('', views.index, name="dash"),
    path('preview', views.preview, name="preview"),
    path('history', views.history, name="history"),
    path('history/<str:term>', views.history)
]