from django.db import models
from django.utils import timezone

class Person(models.Model):
    pass

class Deals(models.Model):
    current_id = models.IntegerField(default=0)
    current_owner_name = models.CharField(default="-", max_length=155)
    current_stage_id = models.IntegerField(default=0)
    current_active = models.BooleanField(default=False)
    current_status = models.CharField(default="-", max_length=15)
    current_person_id = models.IntegerField(default=0)
    current_person_name = models.CharField(default="-", max_length=155)
    current_pipeline_id = models.IntegerField(default=0)
    current_title = models.CharField(default="-", max_length=155)
    current_org_name = models.CharField(default="-", max_length=155)
    current_weighted_value = models.FloatField(default=0.0)
    current_value = models.FloatField(default=0.0)
    current_update_time = models.DateTimeField(default=timezone.now)
    current_add_time = models.DateTimeField(default=timezone.now)

