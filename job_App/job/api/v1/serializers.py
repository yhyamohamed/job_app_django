from job.models import Job
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Job


class JobCreationSerializer(serializers.ModelSerializer):

    # created_by = serializers.HiddenField(
    #     default = serializers.CurrentUserDefault(),
    # )

    class Meta:
        fields = 'name', 'description', 'created_by'
        model = Job
