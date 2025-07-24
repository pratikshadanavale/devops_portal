from django.db import models

class ReportLog(models.Model):
    title = models.CharField(max_length=300)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    report_file = models.FileField(upload_to='reports/')
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.status} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"

