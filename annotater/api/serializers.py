from rest_framework import serializers
from .models import Annotation


class AnnotationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annotation
        fields = ['resolvable_object_id', 'key', 'value', 'source', 'notes', 'created_date']
