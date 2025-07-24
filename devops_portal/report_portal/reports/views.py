from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
import os

from .models import ReportLog
from .forms import ReportForm

def upload_report(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Report uploaded successfully")
            return redirect('report-history')
    else:
        form = ReportForm()
    return render(request, 'report_portal/upload.html', {'form': form})


def report_history(request):
    reports = ReportLog.objects.all().order_by('-uploaded_at')

    print("Template directories:", settings.TEMPLATES[0]['DIRS'])
    return render(request, 'report_portal/history.html', {'reports': reports})



def home(request):
    return HttpResponse("Welcome to the Report Portal!")




