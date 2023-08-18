from django.db import models


class Deals(models.Model):
    deal_id = models.IntegerField()
    deal_name = models.CharField(max_length=155)

    person_id = models.IntegerField()
    person_name = models.CharField(max_length=155)
    person_phone = models.CharField(max_length=25)
    person_email = models.EmailField(max_length=55)

    class Meta:
        indexes = [
            models.Index(fields=["deal_id", "deal_name"])
        ]

