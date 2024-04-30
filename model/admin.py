from django.contrib import admin
from .models import Model, Text


class AdminModel(admin.ModelAdmin):
    pass


class AdminText(admin.ModelAdmin):
    pass


admin.site.register(Model, AdminModel)
admin.site.register(Text, AdminText)