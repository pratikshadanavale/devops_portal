from django.urls import path
from .views import ingest_jenkins_log

urlpatterns = [
    path('api/logs/', ingest_jenkins_log, name='ingest_jenkins_log'),
]
