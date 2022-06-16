from rest_framework import serializers

from accounts.api.v1.serializers import UserSerializer
from ...models import Job


class JobSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    applied_developers = UserSerializer(many=True)
    developer = UserSerializer()

    class Meta:
        fields = '__all__'
        model = Job
        depth = 1


class JobCreationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = 'name', 'description', 'tags'
        model = Job

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        job = Job(
            created_by=self.context['request'].user,
            **validated_data
        )
        job.save()
        job.tags.set(tags)
        return job
