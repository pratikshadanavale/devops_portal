from django.db import models

class JenkinsCILog(models.Model):
    job_name = models.CharField(max_length=255)
    build_no = models.IntegerField()
    status = models.CharField(max_length=50)
    #timestamp = models.DateTimeField(auto_now_add=True)
    log_output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_name} - Build #{self.build_no} - {self.status}"
