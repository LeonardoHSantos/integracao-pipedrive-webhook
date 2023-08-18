from . import views
from django.urls import path

urlpatterns = [
    path("webhook/v1/deals/", views.Deals, name="deals")
]
