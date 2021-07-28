from django.shortcuts import render
from rest_framework import viewsets, renderers, pagination
from .serializers import AnnotationSerializer
from .models import Annotation


class AnnotationViewSet(viewsets.ModelViewSet):
    """
    GBIF Norway's annotation service adds annotations to objects available in the resolver.
    """
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    pagination_class = pagination.LimitOffsetPagination
    renderer_classes = (renderers.JSONRenderer, renderers.BrowsableAPIRenderer)
    filter_fields = ('resolvable_object_id', 'key', 'value', 'source', 'notes', 'created_date')
