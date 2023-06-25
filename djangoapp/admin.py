from django.contrib import admin
from .models import ProfileClient


@admin.register(ProfileClient)
class ProfileClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'tax_id', 'loan_value', 'status')
