from django.http import JsonResponse
from django.conf import settings
from rajan_nse import Strategies
import pandas as pd

CANDLESTICK_PATTERN_DIR = "./api/data"
BULLISH_ENGULLFING_FILE = 'bullishEngullfing.csv'
DOJI_FILE = 'doji.csv'
FALLING_WEDGE_FILE = 'fallingWedge.csv'
RISING_WEDGE_FILE = 'risingWedge.csv'
HAMMER_FILE = 'hammer.csv'
NEAR_52WEEK_HIGH_FILE = 'near52WeekHigh.csv'
NEAR_52WEEK_LOW_FILE = 'near52WeekLow.csv'

def version(request):
    return JsonResponse({'version': settings.API_VERSION})

def get_oi_gainers(request):
    strategies = Strategies()
    data = strategies.oiSpurtsFilteredGainerStocks()
    return JsonResponse({'data': data})

def get_oi_losers(request):
    strategies = Strategies()
    data = strategies.oiSpurtsFilteredLoserStocks()
    return JsonResponse({'data': data})

# TODO: Use caching of this request
def get_promoter_buyback(request):
    strategies = Strategies()
    data = strategies.promoterBuyBackStocks()
    return JsonResponse({'data': data})

def get_bullish_engullfing(request):
    df = pd.read_csv(CANDLESTICK_PATTERN_DIR + '/' + BULLISH_ENGULLFING_FILE)
    return JsonResponse({'data': df['0'].tolist()})

def get_doji(request):
    df = pd.read_csv(CANDLESTICK_PATTERN_DIR + '/' + DOJI_FILE)
    return JsonResponse({'data': df['0'].tolist()})

def get_falling_wedge(request):
    df = pd.read_csv(CANDLESTICK_PATTERN_DIR + '/' + FALLING_WEDGE_FILE)
    return JsonResponse({'data': df['0'].tolist()})

def get_rising_wedge(request):
    df = pd.read_csv(CANDLESTICK_PATTERN_DIR + '/' + RISING_WEDGE_FILE)
    return JsonResponse({'data': df['0'].tolist()})

def get_hammer(request):
    df = pd.read_csv(CANDLESTICK_PATTERN_DIR + '/' + HAMMER_FILE)
    return JsonResponse({'data': df['0'].tolist()})

def get_near_52week_high(request):
    df = pd.read_csv(CANDLESTICK_PATTERN_DIR + '/' + NEAR_52WEEK_HIGH_FILE)
    return JsonResponse({'data': df['0'].tolist()})

def get_near_52week_low(request):
    df = pd.read_csv(CANDLESTICK_PATTERN_DIR + '/' + NEAR_52WEEK_LOW_FILE)
    return JsonResponse({'data': df['0'].tolist()})
