from django.http import HttpResponse
from django.template import loader
from django.conf import settings

def index(request):
    template = loader.get_template('master.html')
    context = {
        "API_BASE_URL": settings.API_BASE_URL
    }
    return HttpResponse(template.render(context, request))
