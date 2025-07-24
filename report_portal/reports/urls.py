
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_report, name='upload-report'),
    path('history/', views.report_history, name='report-history'),
    path('', views.home, name='home'),

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)