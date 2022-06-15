from job.models import Job
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Job
        depth=1


class JobCreationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = 'name', 'description', 'created_by'
        model = Job
