

from django.contrib import admin
from .models import JenkinsCILog # for ci_logs app

@admin.register(JenkinsCILog)
class JenkinsCILogAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_name', 'status', 'created_at')  # show these columns
    search_fields = ('job_name', 'status')
    list_filter = ('status', 'created_at')

