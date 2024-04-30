from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from controller.certificate import CertificateController
from controller.pdf import PDFController
from .models import Certificate
from model.models import Model
from django.views.decorators.csrf import csrf_exempt
import json

def make_pdf(request, pk: int):
    certificate = Certificate.objects.filter(pk=pk).first()
    img_bytes = CertificateController.make(certificate, 'JPEG', 50, True)
    pdf_bytes = PDFController.make(img_bytes)
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="meu_pdf.pdf"'
    return response

@csrf_exempt
def make_preview(request):
    if request.method == "POST":
        data_str = request.body.decode('utf-8')
        data_json = json.loads(data_str)
        _model = Model.objects.get(pk=data_json['model'])
        certificate = Certificate(identifier='', model=_model, data_json=data_str)
        img_bytes = CertificateController.make(certificate, 'JPEG', 50)
        response = HttpResponse(img_bytes.front, content_type="image/jpeg")
        return response

@csrf_exempt
def make_certificate(request):
    if request.method == "POST":
        data_str = request.body.decode('utf-8')
        data_json = json.loads(data_str)
        _model = Model.objects.get(pk=data_json['model'])
        del data_json['model']
        _identifier = ''
        for _, value in data_json.items():
            _identifier += value
        Certificate(identifier=_identifier, model=_model, data_json=str(data_json)).save()
        return JsonResponse({"ok": "ok"})