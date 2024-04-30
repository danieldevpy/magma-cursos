from django.urls import path
from certificate import views

urlpatterns = [
    path('make_pdf/<int:pk>', views.make_pdf),
    path('make_preview', views.make_preview),
    path('make_certificate', views.make_certificate),
    path('validate/<int:pk>', views.validate)
]