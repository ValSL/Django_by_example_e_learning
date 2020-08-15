from rest_framework import serializers
from ..models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Subject"""
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']
