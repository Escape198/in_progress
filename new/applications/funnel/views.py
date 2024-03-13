import datetime
import traceback

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from applications.log.views import send_telegram_message
from applications.funnel.handler import handler
from applications.funnel.models import Lead


@csrf_exempt
def new_form(request):
    if request.method == 'POST':
        if True:
            lead = handler(request.POST)
    return render(request, 'payment.html', {'lead': lead})
