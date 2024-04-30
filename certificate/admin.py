from django.contrib import admin
from .models import Certificate


class AdminCertificate(admin.ModelAdmin):
    pass


admin.site.register(Certificate, AdminCertificate)


{
    "name": "Daniel Fernandes Pereira",
    "cpf": "187.149.337-48",
    "extra": "Nova Iguaçu, 29/04/2024"
}