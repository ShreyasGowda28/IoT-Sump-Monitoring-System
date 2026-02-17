from django.contrib import admin
from .models import SumpReading


@admin.register(SumpReading)
class SumpReadingAdmin(admin.ModelAdmin):
    list_display = ("water_level", "mud_level", "leakage_current", "motor_status", "timestamp")
