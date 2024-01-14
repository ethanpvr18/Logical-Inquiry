from django.contrib import admin
from .models import LineItem


class LineItemAdmin(admin.ModelAdmin):
    list_display = ('line_number', 'formula', 'justification', 'assumption_dependence')


admin.site.register(LineItem, LineItemAdmin)