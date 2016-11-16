from rest_framework import serializers

class DatasSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()