
from django.contrib import admin
from .models import ReportLog

@admin.register(ReportLog)
class ReportLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_file', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('report_file', 'status')

