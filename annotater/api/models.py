from django.db import models

class Annotation(models.Model):
    resolvable_object_id = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=800)
    source = models.CharField(max_length=200, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
