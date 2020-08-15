from rest_framework import serializers
from ..models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Subject
    Запаковка в JSON
    """
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']
