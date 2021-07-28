from django.db import models

class Annotation(models.Model):
    id = models.CharField(max_length=200, primary_key=True, serialize=False)
    resolvable_object_id = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=800)
    source = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    deleted_date = models.DateField(null=True, blank=True)
