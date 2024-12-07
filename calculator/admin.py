from django.contrib import admin
from .models import Calculator

# Register your models here.
class CalculatorAdmin(admin.ModelAdmin):
    list_display = ["value_1", "value_2", "outout", "created_at"]
    list_filter = ['hint', 'created_at']
    date_hierarchy = 'created_at'

admin.site.register(Calculator, CalculatorAdmin)
