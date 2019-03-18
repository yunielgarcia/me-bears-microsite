from rest_framework import serializers
from .models import Content


class ContentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
