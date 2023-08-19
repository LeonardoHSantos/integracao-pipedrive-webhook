from django.db import models
from django.utils import timezone

class Person(models.Model):
    current_person_id = models.IntegerField(default=0)
    current_person_name = models.CharField(default="-", max_length=155)
    current_person_owner_name = models.CharField(default="-", max_length=155)
    current_person_open_deals_count = models.IntegerField(default=0)
    current_person_email = models.CharField(default="-", max_length=55)
    current_person_phone = models.CharField(default="-", max_length=25)
    current_person_add_time = models.DateTimeField(default=timezone.now)
    current_person_update_time = models.DateTimeField(default=timezone.now)

class Deals(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
    current_deal_id = models.IntegerField(default=0)
    current_deal_owner_name = models.CharField(default="-", max_length=155)
    current_deal_stage_id = models.IntegerField(default=0)
    current_deal_active = models.BooleanField(default=False)
    current_deal_status = models.CharField(default="-", max_length=15)
    current_deal_person_id = models.IntegerField(default=0)
    current_deal_person_name = models.CharField(default="-", max_length=155)
    current_deal_pipeline_id = models.IntegerField(default=0)
    current_deal_title = models.CharField(default="-", max_length=155)
    current_deal_org_name = models.CharField(default="-", max_length=155)
    current_deal_weighted_value = models.FloatField(default=0.0)
    current_deal_value = models.FloatField(default=0.0)
    current_deal_update_time = models.DateTimeField(default=timezone.now)
    current_deal_add_time = models.DateTimeField(default=timezone.now)

