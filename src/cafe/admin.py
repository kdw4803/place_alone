from django.contrib import admin
from .models import Cafe,Survey

# Register your models here.
@admin.register(Cafe,Survey)
class AuthorAdmin(admin.ModelAdmin):
    pass