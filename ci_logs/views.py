from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import JenkinsCILog
from .serializers import JenkinsLogSerializer

@api_view(['POST'])
def ingest_jenkins_log(request):
    serializer = JenkinsLogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Log saved successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
