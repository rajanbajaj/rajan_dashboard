from django.http import JsonResponse
from django.conf import settings
from rajan_nse import Strategies

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
