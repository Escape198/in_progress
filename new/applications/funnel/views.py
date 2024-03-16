import datetime
import traceback

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from applications.log.views import send_telegram_message
from applications.funnel.models.lead import Lead


@csrf_exempt
def new_form(request) -> render:
    if request.method == 'POST':
        if True: # Fraud filter
            lead = Lead()
            lead.setattr_request(request.POST)

            if not lead.check_required_fields([
                lead.name, lead.phone, lead.email]
            ):
                return HttpResponse(400, status=400)
            response = render(request, 'funnel/payment.html', {'lead': lead})
    else:
        response = render(request, 'funnel/payment.html')
    return response
