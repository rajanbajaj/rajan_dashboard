from django.urls import path

from .controllers.controller import *

urlpatterns = [
    path("", version, name="api.version"),
    path("oi-gainers", get_oi_gainers, name="api.oi_gainers"),
    path("oi-losers", get_oi_losers, name="api.oi_losers"),
    path("promoter-buyback", get_promoter_buyback, name="api.promoter_buyback"),
    path("bullish-engullfing", get_bullish_engullfing, name="api.bullish_engullfing"),
    path('doji', get_doji, name="api.doji"),
    path('falling-wedge', get_falling_wedge, name="api.falling_wedge"),
    path('rising-wedge', get_rising_wedge, name='api.rising_wedge'),
    path('hammer', get_hammer, name='api.hammer'),
    path('near-52week-high', get_near_52week_high, name='api.near_52week_high'),
    path('near-52week-low', get_near_52week_low, name='api.near_52week_low'),
    path('hammer/<symbol>', is_symbol_forms_hammer, name='api.hammer.symbol'),
    path('watchlist/add/<symbol>', add_to_watchlist, name='api.watchlist.add'),
    path('watchlist/remove/<symbol>', add_to_watchlist, name='api.watchlist.remove'),
    path('watchlist/clear', add_to_watchlist, name='api.watchlist.clear'),
    path('watchlist/get', get_watchlist, name='api.watchlist.get'),
    path('watchlist/has/<symbol>', has_watchlist, name='api.watchlist.has'),
]
