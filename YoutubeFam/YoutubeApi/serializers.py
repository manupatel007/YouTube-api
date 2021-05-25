from .models import YoutubeData
from rest_framework import serializers

class YTSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeData
        fields = ['thumbnail','title','description','publish_time','video_id']