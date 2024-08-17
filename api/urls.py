from django.urls import path

from .controllers.controller import *

urlpatterns = [
    path("", version, name="api.version"),
    path("oi-gainers", get_oi_gainers, name="api.oi_gainers"),
    path("oi-losers", get_oi_losers, name="api.oi_losers"),
    path("promoter-buyback", get_promoter_buyback, name="api.promoter_buyback"),
]