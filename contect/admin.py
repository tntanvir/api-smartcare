from django.contrib import admin
from .models import Contect

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','phone','problems']

admin.site.register(Contect, ContactAdmin)
