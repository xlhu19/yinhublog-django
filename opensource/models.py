from django.db import models

# Create your models here.
class OpenSourceItem(models.Model):
    o_name = models.CharField(max_length=300)
    o_type = models.CharField(max_length=300)
    o_version = models.CharField(max_length=300)
    o_description = models.TextField()
    o_views = models.PositiveIntegerField(null=False, blank=False, default=0)

