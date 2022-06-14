from rest_framework import serializers
from ...models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Job


class JobCreationSerializer(serializers.ModelSerializer):

    # created_by = serializers.HiddenField(
    #     default = serializers.CurrentUserDefault(),
    # )

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
