from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Model
# Create your views here.
def get_models(request):
    models = Model.objects.all()
    return JsonResponse({"models": [model.to_json() for model in models]})