from django.http import JsonResponse
from django.conf import settings

def index(request):
    return JsonResponse({'version': settings.API_VERSION})