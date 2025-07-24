from django import forms
from .models import ReportLog

class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportLog
        fields = ['title', 'report_file', 'status']
