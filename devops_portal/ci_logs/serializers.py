
from rest_framework import serializers
from .models import JenkinsCILog

class JenkinsLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenkinsCILog
        fields = '__all__'
        extra_kwargs = {
            'build_no': {'required': False},
            'log_output': {'required': False},
        }
