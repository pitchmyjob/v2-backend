from rest_framework import serializers
from backend.apps.job.models import Job, JobQuestion
from backend.authentification.models import User
from backend.libs.media import Base64ImageField


class JobQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobQuestion

class JobSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    def create(self, validated_data):
        image = None
        del validated_data['contracts']
        del validated_data['contract_time']
        if "image" in validated_data:
            image = validated_data['image']
            del validated_data['image']

        job = Job.objects.create(pro = self.context.get('request').user.pro, **validated_data)
        if image :
            job.image = image
            job.save()

        return job

    class Meta:
        model = Job
        exclude = ('pro',)