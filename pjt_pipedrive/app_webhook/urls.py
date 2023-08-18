from . import views
from django.urls import path

urlpatterns = [
    path("pipedrive/v1/deals/", views.PipedriveDeals, name="deals")
]
